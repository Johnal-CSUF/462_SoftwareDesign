'use strict';var appRoot=setAppRoot("mini-inventory-and-sales-management-system","mini-inventory-and-sales-management-system");var spinnerClass='fa fa-spinner faa-spin animated';$(document).ready(function(){$('[data-toggle="tooltip"]').tooltip();totalEarnedToday();$("#transListTable").on('click','.vtr',function(){vtr_(this);});$('form').on('change','.checkField',function(){var errSpan="#"+$(this).attr('id')+"Err";if($(this).val()){$(errSpan).html('');}
else{$(errSpan).html('required');}});$("#transReceiptModal").on('click','.ptr',function(){ptr_();});$(".closeLogInModal").click(function(){window.location.href=appRoot;});$("#loginModalSubmit").click(function(e){e.preventDefault();var email=$("#logInModalEmail").val();var password=$("#logInModalPassword").val();if(!email||!password){$("#logInModalFMsg").css('color','red').html("Please enter both your email and password");return;}
$("#logInModalFMsg").css('color','black').html("Authenticating. Please wait...");handleLogin(email,password,function(returnedData){if(returnedData.status===1){$("#logInModalFMsg").css('color','green').html(returnedData.msg);setTimeout(function(){window.location.reload();},1000);}
else{$("#logInModalFMsg").css('color','red').html(returnedData.msg);}});});$("#importdb").click(function(e){e.preventDefault();$("#selecteddbfile").click();});$("#selecteddbfile").change(function(e){e.preventDefault();var file=$("#selecteddbfile").get(0).files[0];if(file){var formData=new FormData();formData.append('dbfile',file);$("#dbFileMsg").css('color','black').html("Importing database");$.ajax({url:appRoot+"misc/importdb",method:"POST",data:formData,cache:false,processData:false,contentType:false}).done(function(rd){$("#selecteddbfile").val("");if(rd.status===1){$("#dbFileMsg").css('color','green').html("Database successfully imported");setTimeout(function(){$("#dbFileMsg").html("");},3000);}
else{$("#dbFileMsg").css('color','red').html(rd.msg);}}).fail(function(){});}});});function ptr_(){$("#transReceiptToPrint").css({fontSize:'8px'});window.print();$("#transReceiptModal").modal('hide');}
function changeClassName(elementId,newClassName){if(typeof(elementId)==="string"){$("#"+elementId).attr('class',newClassName);}
else{var i;for(i in elementId){$("#"+elementId[i]).attr('class',newClassName);}}
return "";}
function changeInnerHTML(elementId,newValue){if(typeof(elementId)==="string"){$("#"+elementId).html(newValue);}
else{var i;for(i in elementId){$("#"+elementId[i]).html(newValue);}}
return "";}
function changeElementValue(elementId,newValue){if(typeof(elementId)==="string"){$("#"+elementId).val(newValue);}
else{var i;for(i in elementId){$("#"+elementId[i]).val(newValue);}}
return "";}
function loadPage(urlToLoad){$.ajax({type:"GET",url:appRoot+urlToLoad,success:function(returnedData){document.getElementById('pageContent').innerHTML=returnedData.pageContent;document.getElementById('pageTitle').innerHTML=returnedData.pageTitle;}});}
function formChanges(form){if(typeof(form)==="string"){form=document.getElementById(form);}
if(!form||!form.nodeName||form.nodeName.toLowerCase()!=="form"){return null;}
var changed=[],n,c,def,o,ol,opt;for(var e=0,el=form.elements.length;e<el;e++){n=form.elements[e];c=false;switch(n.nodeName.toLowerCase()){case "select":def=0;for(o=0,ol=n.options.length;o<ol;o++){opt=n.options[o];c=c||(opt.selected!==opt.defaultSelected);if(opt.defaultSelected){def=o;}}
if(c&&!n.multiple){c=(def!==n.selectedIndex);}
break;case "textarea":case "input":switch(n.type.toLowerCase()){case "checkbox":case "radio":c=(n.checked!==n.defaultChecked);break;default:c=(n.value!==n.defaultValue);break;}
break;}
if(c){changed.push(n);}}
if(changed.length>0){return true;}
else{return false;}}
function displayFlashMsg(msg,iconClassName,color,time){changeClassName('flashMsgIcon',iconClassName);$("#flashMsg").css('color',color);changeInnerHTML('flashMsg',msg);$("#flashMsgModal").modal('show');if(time){setTimeout(function(){$("#flashMsgModal").modal('hide');},time);}}
function hideFlashMsg(){changeClassName('flashMsgIcon',"");$("#flashMsg").css('color','');changeInnerHTML('flashMsg',"");$("#flashMsgModal").modal('hide');}
function changeFlashMsgContent(msg,iconClassName,color,time){changeClassName('flashMsgIcon',iconClassName);$("#flashMsg").css('color',color);changeInnerHTML('flashMsg',msg);if(time){setTimeout(function(){$("#flashMsgModal").modal('hide');},time);}}
function tc_(elemId){$("#"+elemId).attr("class","active");}
function numOnly(value,elementId){$("#"+elementId).val(value.replace(/\D+/g,""));}
function stopInterval(intervalObj){clearInterval(intervalObj);}
function randomString(length){var rand=Math.random().toString(36).slice(2).substring(0,length);return rand;}
function vtr_(elem){var ref=elem.innerHTML;if(ref){$("#transReceipt").html("<i class='fa fa-spinner faa-spin animated'></i> Loading receipt");$("#transReceiptModal").modal('show');$.ajax({url:appRoot+"transactions/vtr_",type:"post",data:{ref:ref},success:function(returnedData){if(returnedData.status===1){$("#transReceipt").html(returnedData.transReceipt);}
else{$("#transReceipt").html("Transaction not found");}}});}}
function drm_(){$("#transReceiptModal").modal("hide");}
function totalEarnedToday(){$.ajax({method:"POST",url:appRoot+"misc/totalearnedtoday"}).done(function(returnedData){$("#totalEarnedToday").html(returnedData.totalEarnedToday);});}
function checkField(value,errorElementId){if(value){$("#"+errorElementId).html('');}
else{$("#"+errorElementId).html('required');}}
function checkDocumentVisibility(functionToCall){var hidden="hidden";if(hidden in document){$(document).on("visibilitychange",functionToCall);}
else if((hidden="mozHidden")in document){document.addEventListener("mozvisibilitychange",functionToCall);}
else if((hidden="webkitHidden")in document){document.addEventListener("webkitvisibilitychange",functionToCall);}
else if((hidden="msHidden")in document){document.addEventListener("msvisibilitychange",functionToCall);}
else if("onfocusout"in document){document.onfocusin=document.onfocusout=functionToCall;}
else{window.onpageshow=window.onpagehide=window.onfocus=window.onblur=functionToCall;}}
function checkLogin(){if(document.hidden||document.onfocusout||window.onpagehide||window.onblur){console.log("Window has lost focus");}
else{$.ajax({url:appRoot+"access/css",method:"GET"}).done(function(returnedData){if(returnedData.status===0){$("#logInModalFMsg").css('color','red').html("Your session has expired. Please log in to continue");$("#logInModal").modal("show");}});}}
function handleLogin(email,password,callback){var jsonToReturn="";$.ajax(appRoot+'access/login',{method:"POST",data:{email:email,password:password}}).done(function(returnedData){if(returnedData.status===1){jsonToReturn={status:1,msg:"Authenticated..."};}
else{jsonToReturn={status:0,msg:"Invalid email/password combination"};}
typeof(callback)==="function"?callback(jsonToReturn):"";}).fail(function(){var msg="Log in failed. Please check your internet connection and try again later.";jsonToReturn={status:0,msg:msg};typeof(callback)==="function"?callback(jsonToReturn):"";});}
function checkBrowserOnline(changeFlashContent){if((!navigator.onLine)&&(appRoot.search('localhost')===-1)){changeFlashContent?changeFlashMsgContent('Network Error! Please check your internet connection and try again','','red','',false):displayFlashMsg('Network Error! Please check your internet connection and try again','','red','',false);}
else{changeFlashContent?changeFlashMsgContent('Oops! Bug? Unable to process your request. Please try again or report error','','red','',false):displayFlashMsg('Oops! Bug? Unable to process your request. Please try again or report error','','red','',false);}}
function setAppRoot(devFolderName,prodFolderName){var hostname=window.location.hostname;var devFolder=devFolderName?devFolderName+"/":"";var prodFolder=prodFolderName?prodFolderName+"/":"";var baseURL="";if(hostname.search("localhost")!==-1||(hostname.search("192.168.")!==-1)||(hostname.search("127.0.0.")!==-1)){baseURL=window.location.origin+"/"+devFolder;}
else{baseURL=window.location.origin+"/"+prodFolder;}
return baseURL;}
function inArray(value,array){for(let i=0;i<array.length;i++){if(array[i].trim()===value.trim()){return true;}}
return false;}
function arrayUnique(array){var newArray=[];for(let i=0;i<array.length;i++){if(inArray(array[i].trim(),newArray)){continue;}
newArray.push(array[i].trim());}
return newArray;}