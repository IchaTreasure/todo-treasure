{"filter":false,"title":"urls.py","tooltip":"/django_todo/urls.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["#"],"id":57}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["#"],"id":58}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":["o"],"id":60}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"remove","lines":["o"],"id":61}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["#"],"id":62}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["#"],"id":63}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":35},"action":"remove","lines":["list"],"id":64},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":["_"]}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["0"],"id":65}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":["0"],"id":66}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["o"],"id":67}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":32},"action":"remove","lines":["_list "],"id":68},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":30},"action":"remove","lines":["#from todo.views import say_hello","#from todo.views import say_hi"],"id":69}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":26},"action":"remove","lines":["    #url(r'^$', say_hello),","    #url(r'^hi$', say_hi),"],"id":70}],[{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"remove","lines":["o"],"id":71},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"remove","lines":["d"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["o"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"remove","lines":["t"]}],[{"start":{"row":21,"column":37},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":72}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":73}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"remove","lines":["\"\"\"django_todo URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo)","]",""],"id":74},{"start":{"row":0,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list, create_an_item","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list),","    url(r'^add$', create_an_item)","]"]}],[{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":[","],"id":75}],[{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":[" "],"id":76},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["e"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":["d"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":["i"]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":[" "],"id":77}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"remove","lines":[" "],"id":78}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":["_"],"id":79},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":["a"]},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"remove","lines":[" "],"id":81}],[{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["i"],"id":82},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"insert","lines":["t"]},{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"insert","lines":["e"]},{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"insert","lines":["m"]}],[{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"remove","lines":["m"],"id":83},{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"remove","lines":["e"]},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"remove","lines":["t"]},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"remove","lines":["i"]}],[{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["_"],"id":84},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"insert","lines":["i"]},{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"insert","lines":["t"]},{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"insert","lines":["e"]},{"start":{"row":16,"column":65},"end":{"row":16,"column":66},"action":"insert","lines":["m"]}],[{"start":{"row":16,"column":54},"end":{"row":16,"column":66},"action":"remove","lines":["edit_an_item"],"id":85},{"start":{"row":16,"column":54},"end":{"row":16,"column":68},"action":"insert","lines":["edit_an_item()"]}],[{"start":{"row":16,"column":67},"end":{"row":16,"column":68},"action":"remove","lines":[")"],"id":86},{"start":{"row":16,"column":66},"end":{"row":16,"column":67},"action":"remove","lines":["("]}],[{"start":{"row":21,"column":33},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":87},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":33},"action":"insert","lines":["url(r'^add$', create_an_item)"],"id":88}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":31},"action":"remove","lines":["reate_an_ite"],"id":89}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"remove","lines":["c"],"id":90}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"remove","lines":["m"],"id":91}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["e"],"id":92},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":20},"action":"remove","lines":["ed"],"id":93},{"start":{"row":22,"column":18},"end":{"row":22,"column":32},"action":"insert","lines":["edit_an_item()"]}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":32},"action":"remove","lines":["()"],"id":94}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":[")"],"id":95}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":[")"],"id":96}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["d"],"id":97},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":["d"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["a"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["e"],"id":98},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["d"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["i"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["/"],"id":99}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["`"],"id":100}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["`"],"id":101}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["~"],"id":102}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["~"],"id":103}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["\""],"id":104},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["|"]}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"remove","lines":["|"],"id":105},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["\""]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["§"],"id":106}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["§"],"id":107}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["`"],"id":108}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["`"],"id":109}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["'"],"id":110}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["'"],"id":111}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["`"],"id":112}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["`"],"id":113}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["|"],"id":114},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["|"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["|"]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["?"],"id":115},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["?"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":[">"]},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["<"]},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["L"]}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":[":"],"id":116},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["{"]}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":["}"],"id":117},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["]"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["["]},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["'"]}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["'"],"id":118},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["."]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["l"]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":[","]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["."]},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["'"]}],[{"start":{"row":22,"column":36},"end":{"row":22,"column":38},"action":"insert","lines":["[]"],"id":119}],[{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":[";"],"id":120}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":40},"action":"insert","lines":["''"],"id":121}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["]"],"id":122},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["["]}],[{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"insert","lines":["!"],"id":123},{"start":{"row":22,"column":42},"end":{"row":22,"column":43},"action":"insert","lines":["@"]},{"start":{"row":22,"column":43},"end":{"row":22,"column":44},"action":"insert","lines":["£"]},{"start":{"row":22,"column":44},"end":{"row":22,"column":45},"action":"insert","lines":["$"]},{"start":{"row":22,"column":45},"end":{"row":22,"column":46},"action":"insert","lines":["%"]},{"start":{"row":22,"column":46},"end":{"row":22,"column":47},"action":"insert","lines":["^"]}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"insert","lines":["&"],"id":124}],[{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"insert","lines":["*"],"id":125},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"insert","lines":["("]},{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"insert","lines":[")"]}],[{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"insert","lines":["_"],"id":126},{"start":{"row":22,"column":52},"end":{"row":22,"column":53},"action":"insert","lines":["+"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"insert","lines":["-"]},{"start":{"row":22,"column":54},"end":{"row":22,"column":55},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":54},"end":{"row":22,"column":55},"action":"remove","lines":["="],"id":127},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"remove","lines":["-"]},{"start":{"row":22,"column":52},"end":{"row":22,"column":53},"action":"remove","lines":["+"]},{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"remove","lines":["_"]},{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"remove","lines":[")"]},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"remove","lines":["("]},{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"remove","lines":["*"]},{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"remove","lines":["&"]},{"start":{"row":22,"column":46},"end":{"row":22,"column":47},"action":"remove","lines":["^"]},{"start":{"row":22,"column":45},"end":{"row":22,"column":46},"action":"remove","lines":["%"]},{"start":{"row":22,"column":44},"end":{"row":22,"column":45},"action":"remove","lines":["$"]},{"start":{"row":22,"column":43},"end":{"row":22,"column":44},"action":"remove","lines":["£"]},{"start":{"row":22,"column":42},"end":{"row":22,"column":43},"action":"remove","lines":["@"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"remove","lines":["!"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"remove","lines":["["]},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":["]"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":40},"action":"remove","lines":["''"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"remove","lines":[";"]},{"start":{"row":22,"column":36},"end":{"row":22,"column":38},"action":"remove","lines":["[]"]}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"remove","lines":["'"],"id":128},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"remove","lines":["."]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":[","]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["l"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["."]},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["'"]},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["'"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["["]},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"remove","lines":["]"]},{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"remove","lines":["}"]},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"remove","lines":["{"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"remove","lines":[":"]},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"remove","lines":["L"]},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"remove","lines":["<"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"remove","lines":[">"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"remove","lines":["?"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"remove","lines":["?"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"remove","lines":["|"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"remove","lines":["|"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["|"]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["\\"],"id":129}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["d"],"id":130}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["+"],"id":131},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"remove","lines":["s"],"id":132}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["("],"id":133}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":[")"],"id":134}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["?"],"id":135},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["p"]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["<"],"id":136}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["i"],"id":137},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":["d"]},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":[">"]}],[{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":[","],"id":138}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"remove","lines":["?"],"id":139}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["?"],"id":140}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list, create_an_item, edit_an_item","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list),","    url(r'^add$', create_an_item),","    url(r'^edit/(?p<id>\\d+)$', edit_an_item)","]"],"id":141},{"start":{"row":0,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":["","\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list, create_an_item, edit_an_item","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list),","    url(r'^add$', create_an_item),","    url(r'^edit/(?P<id>\\d+)$', edit_an_item)","]"]}],[{"start":{"row":17,"column":66},"end":{"row":17,"column":67},"action":"insert","lines":[","],"id":142}],[{"start":{"row":17,"column":67},"end":{"row":17,"column":68},"action":"insert","lines":[" "],"id":143},{"start":{"row":17,"column":68},"end":{"row":17,"column":69},"action":"insert","lines":["t"]},{"start":{"row":17,"column":69},"end":{"row":17,"column":70},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":68},"end":{"row":17,"column":70},"action":"remove","lines":["to"],"id":144},{"start":{"row":17,"column":68},"end":{"row":17,"column":83},"action":"insert","lines":["toggle_status()"]}],[{"start":{"row":17,"column":81},"end":{"row":17,"column":83},"action":"remove","lines":["()"],"id":145}],[{"start":{"row":17,"column":81},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":146}],[{"start":{"row":22,"column":44},"end":{"row":22,"column":45},"action":"insert","lines":[","],"id":147}],[{"start":{"row":22,"column":45},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":148},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":45},"action":"insert","lines":["url(r'^edit/(?P<id>\\d+)$', edit_an_item),"],"id":149}],[{"start":{"row":23,"column":44},"end":{"row":23,"column":45},"action":"remove","lines":[","],"id":150}],[{"start":{"row":23,"column":32},"end":{"row":23,"column":43},"action":"remove","lines":["dit_an_item"],"id":151},{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"remove","lines":["e"]}],[{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"insert","lines":["t"],"id":152}],[{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"remove","lines":["t"],"id":153},{"start":{"row":23,"column":31},"end":{"row":23,"column":46},"action":"insert","lines":["toggle_status()"]}],[{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"remove","lines":["t"],"id":154},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"remove","lines":["i"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["d"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"remove","lines":["e"]}],[{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["t"],"id":155},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["o"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["g"]},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["g"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["l"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":47},"end":{"row":23,"column":48},"action":"remove","lines":[")"],"id":156},{"start":{"row":23,"column":46},"end":{"row":23,"column":48},"action":"remove","lines":["()"]}],[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":[")"],"id":157}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":18},"end":{"row":9,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589380050724,"hash":"7096ee012a02127b05683be8885bdde13a67a167"}