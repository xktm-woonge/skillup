from django.shortcuts import render

def load_chattion_main_page(request):
    return render(request, 'chatting_main_page/chatting_viewer_page.html')