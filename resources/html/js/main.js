function postaction(){
	var title = document.getElementById("title");
	if(title.value == "") {
		alert("empty");
	}else{
        PyFunction("interface/data/add", JSON.stringify({
            title: title.value
        }), function (data) {
            load();
        })
	}
}

function loadData(){
    PyFunction("interface/data/load/todo", "", function (data) {
        var collection=localStorage.getItem("todo");
        if(collection!=null){
            return JSON.parse(collection);
        }
        else return [];
    });
}

function remove(id){
    PyFunction("interface/data/delete", JSON.stringify({
        id: id
    }), function (data) {
        load();
    });
}

function update(id,status){
    PyFunction("interface/data/modify", JSON.stringify({
        id: id,
        status: status
    }), function (data) {
        load();
    })
}

function edit(i)
{
	load();
	var p = document.getElementById("p-"+i);
	title = p.innerHTML;
	p.innerHTML="<input id='input-"+i+"' value='"+title+"' />";
	var input = document.getElementById("input-"+i);
	input.setSelectionRange(0,input.value.length);
	input.focus();
	input.onblur =function(){
		if(input.value.length == 0){
			p.innerHTML = title;
			alert("empty");
		}
		else{
			update(i,"title",input.value);
		}
	};
}

function load(){
	var todolist=document.getElementById("todolist");
	var donelist=document.getElementById("donelist");
    PyFunction("interface/data/load/all", "", function (data) {
        var data=JSON.parse(data);
		var todoCount=0;
		var doneCount=0;
		var todoString="";
		var doneString="";
		for (var i = data.length - 1; i >= 0; i--) {
		    var itemHtmlString = "<li class='panel panel-default' draggable='true'>"
                                 + "<div class='panel-heading' role='tab' id='heading-" + data[i].id + "'>"
                                 + "<h4 class='panel-title'>"
                                 + "<input type='checkbox' onchange='update(" + data[i].id+ ", " + (data[i].done?"\"todo\"":"\"done\"") + " )' " + (data[i].done?" checked='checked' />":"/>")
                                 + "<a role='button' data-toggle='collapse' data-parent='#accordion' href='#collapse" + data[i].id + "' >" +data[i].title+ "</a>"
                                 + "<a href='javascript:;' class='todomod'>*</a>"
                                 + "<a href='javascript:remove(" + data[i].id + ")' class='tododel'>-</a>"
                                 + "</h4>"
                                 + "<div id='collapse" + data[i].id + "' class='panel-collapse collapse' role='tabpanel'>"
                                 + "<div class='panel-body'>"
                                 + data[i].context
                                 + "</div>"
                                 + "</div>"
                                 + "</li>";
		    if (data[i].done) {
                doneString += itemHtmlString;
                doneCount++;
            } else {
                todoString += itemHtmlString;
                todoCount++;
            }
		};

		todocount.innerHTML=todoCount;
		todolist.innerHTML=todoString;
		donecount.innerHTML=doneCount;
		donelist.innerHTML=doneString;
    });
}

window.onload=load;

