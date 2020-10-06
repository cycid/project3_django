
        	

        	//get csrf from cookies
        	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


	const btn = document.querySelector('#confirm_order');
    var adds=0;
function sendData( data ) {
  const XHR = new XMLHttpRequest(),
        FD  = new FormData();

  // Push our data into our FormData object
  
    FD.append( data );
  

  // Define what happens on successful data submission
  XHR.addEventListener( 'load', function( event ) {
    alert( 'Yeah! Data sent and response loaded.' );
  } );

  // Define what happens in case of error
  XHR.addEventListener(' error', function( event ) {
    alert( 'Oops! Something went wrong.' );
  } );

  // Set up our request
  XHR.open( 'POST', '/makeorder' );

  // Send our FormData object; HTTP headers are set automatically
  XHR.send( FD );
}
//sending data to make order
 function sending_data(){
 document.getElementById("order_form").addEventListener('submit', (b)=>
 	{
   //taking data from input form
        //taking data from checkbox
        var check = document.getElementsByClassName("checkform")
        str=[]
        for(var i=0; i<check.length; i++){
        	if (check[i].checked==true){

        		str.push(check[i].value)
        	}
        }
        adds=JSON.stringify(str)
        id=document.getElementById('form_button').value;
        
        
        amount=document.getElementById('amount').value;
        n=document.getElementById('size')
        size=n.options[n.selectedIndex].value

        
                
        const request = new XMLHttpRequest(),
        FD  = new FormData();
  	    FD.append( "id", id );
  	    FD.append( 'amount', amount );
  	    FD.append( 'size', size );
  	    FD.append( 'adds', adds );
  	    console.log(FD)
  	    request.open( 'POST', '/makeorder' );

  // Send our FormData object; HTTP headers are set automatically
        request.setRequestHeader("X-CSRFToken", csrftoken);
        request.send( FD );
        
        
        
  	    
  	


  	 
    
});
 };

 function add_form(value){

 	const request = new XMLHttpRequest()
 	FD  = new FormData();
  	    FD.append( "id", value);
 	request.open('POST', '/add_form');
 	request.onload = () =>
 	{   id_dish=value
 		data = JSON.parse(request.response);
 		toppings=data.toppings
 		size=data.size
 		adds=data.adds
 		console.log(toppings)
 		const form=document.createElement('form')
 		form.setAttribute('id', 'order_form');
 		form.setAttribute('method', 'POST');
 		size_label=document.createElement('label')
 		size_label.setAttribute('for', 'size')
 		select_size=document.createElement('select')
 		select_size.setAttribute('id', 'size')
 		select_size.setAttribute('name', 'size')
 		select_size.setAttribute('class', 'list_size')
 		    if (size=="standart") {
 			    select_menu=document.createElement('option')
 			    select_menu.setAttribute('value', 'standart')
 			    select_menu.innerHTML ="standart"
 			    select_size.appendChild(select_menu)
 		    }
 		    else {
 			    select_menu1=document.createElement('option')
 			    select_menu1.setAttribute('value', 'small')
 			    select_menu1.innerHTML="small"
 			    select_menu2=document.createElement('option')
 			    select_menu2.setAttribute('value', 'large')
 			    select_menu2.innerHTML="large"
 			    select_size.appendChild(select_menu1)
 			    select_size.appendChild(select_menu2)
 		    }
        amount=document.createElement('input');
        amount.setAttribute('type', 'number');
        amount.setAttribute('min', '0')
        amount.setAttribute('id', 'amount')
        amount.setAttribute('step', '1')
        amount.setAttribute('placeholder', 'quantity');
        topping_list=document.createElement('div')
        toppings.forEach(a => choose_topping(a));
        butn=document.createElement('button')
        butn.setAttribute('id', 'form_button')
        butn.setAttribute('value', value)
        butn.setAttribute('type', 'submit')
        butn.innerHTML='Submit'
        var inputElem = document.createElement('input');
inputElem.type = 'hidden';
inputElem.name = 'csrfmiddlewaretoken';
inputElem.value = '{{ csrf_token }}';

        

        


        form.appendChild(size_label)
        form.appendChild(select_size)
        form.appendChild(amount)
        form.appendChild(topping_list)
        form.appendChild(butn)
        form.appendChild(inputElem);
        
        document.getElementById(id_dish).appendChild(form)
        checkform_limit()
        sending_data()
        as=document.getElementsByClassName('adding_form')
        Array.from(as).forEach(b=>{
          b.disabled=true;
        })


 	}
 	
 	request.setRequestHeader("X-CSRFToken", csrftoken);
 	
 	
 	request.send(FD)
 	



 }
 
 function checkform_limit()
 {  var max = adds;
 	
 	chain=document.getElementsByClassName("checkform")
 	for (var i=0;i<chain.length; i++)
 	{
    
    
 
    chain[i].addEventListener('click', function() {
    	
    	var checkedChecks = document.querySelectorAll(".checkform:checked");
    	 
        if (checkedChecks.length > max)
  	    
  	 	alert("choose properly amount of adds")
        return false;
                
            });
 }
}

 

 //function of adding elements to checkbox(toppings)
function choose_topping(value)
   {
   	container=document.createElement('div')
   	element=document.createElement('input')
   	element.setAttribute('type', 'checkbox')
   	element.classList.add("checkform")
   	element.setAttribute('name', value)
   	element.setAttribute('value', value)
   	label_element=document.createElement('label')
   	label_element.setAttribute('for', value)
   	label_element.innerHTML=value
   	container.appendChild(element)
   	container.appendChild(label_element)
   	topping_list.appendChild(container)



}
//document.getElementById('.checkform').addEventListener('change', checkform_limit)
//functiom for adding dish to users order
function order_dish()
{
	var row=[];
  	    
        


}
	
