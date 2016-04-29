function show(element){
    var description = element.getElementsByClassName("description")[0]
    if (description.style.visibility == 'visible')
	description.style.visibility='hidden';
    else
	description.style.visibility='visible';
}
