from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import PDFForm
from .models import Documento
import fitz
import os

def upload_pdf(request):

    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)

        if form.is_valid():

            arquivo = request.FILES['pdf']

            texto_extraido = ""
            
            pdf = fitz.open(
                stream=arquivo.read(),
                filetype="pdf"
            )
            for pagina in pdf:
                texto_extraido += pagina.get_text()

            pdf.close()

            texto_extraido = " ".join(texto_extraido.splitlines())

            documento = Documento.objects.create(
                nome=arquivo.name,
                pdf=arquivo,
                texto=texto_extraido
            )

            pasta_txt = os.path.join(settings.MEDIA_ROOT, "txts")
            os.makedirs(pasta_txt, exist_ok=True)

            nome_txt = arquivo.name.replace(".pdf", ".txt")

            caminho_txt = os.path.join(
                pasta_txt,
                nome_txt
            )

            with open(caminho_txt, "w", encoding="utf-8") as txt:
                txt.write(texto_extraido)

            txt_url = f"/media/txts/{nome_txt}"

            return render(request, "resultado.html", {
                "texto": texto_extraido,
                "txt_url": txt_url
            })

    else:
        form = PDFForm()

    return render(request, "upload.html", {
        "form": form
    })
