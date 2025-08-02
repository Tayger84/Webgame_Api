from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from . import models
from bs4 import BeautifulSoup
from .services.parser import ali_view_get_and_save, ali_table_get_and_save
import io

def index(request):
    return render(request, 'aliance/index.html')

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. get files from forms
            ali_view_file = ali_view_get_and_save(form.cleaned_data.get('ali_view'))
            ali_detail_file = ali_table_get_and_save(form.cleaned_data.get('ali_detail'))


        # # 2.a) get ali_view file if it was sent (optional in form)
        # if ali_view_file:
        #     html = ali_view_file.read().decode("utf-8")
        #     soup = BeautifulSoup(html, "html.parser")
        #     ali_table = soup.find("table", class_="vis_tbl")
        #     ali_name_div = soup.find(id="icontent")
        #     ali_name = ali_name_div.h1.text

        #     if ali_table:
        #         for row in ali_table.find_all("td", class_="l"):
        #             zeme = "".join(row.text)
        #             print(zeme)
        #     print(ali_name)


        # # 2.b) get ali_detail file (requiered in form)
        # html = ali_detail_file.read().decode("utf-8")
        # soup = BeautifulSoup(html, "html.parser")
        # detail_table = soup.find("table", class_="vis_tbl") # get a whole table wit data

        # if detail_table:
        #     for row in detail_table.find_all("tr")[1:]:
        #         cols = []
        #         for col in row.find_all("td"):
        #             cols.append(col.text.strip())
                    


        #         # print(cols)
        
        return render(request, "aliance/upload.html", {
            'upload_file': form
        })




    else:     
        form = UploadFileForm()
        return render(request, 'aliance/upload.html', {
            'upload_file': form 
            })
