var me = {};
var you = {};

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +                        
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +                        
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control);

        }, time);
    
}

function generic(who,text)
{
    console.log(text);
    for(i=0;i<text.length;i++)
        insertChat(who,text[i]);
}

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keyup", function(e){
    console.log("mytext");
    if (e.which == 13){
        var text = $(this).val();
        if (text != ""){
            insertChat("you", text);
            $.ajax({
      type: "POST",
      url: "/parse_data",
      data: JSON.stringify(text),
      contentType: "application/json",
      success: function(data){
        console.log(data.lis);
        if(data.lis==9999)
            location.reload();

        for(i=0;i<data.lis.length;i++)
            insertChat("me",data.lis[i]);            
      },
      failure: function(msg){
        console.log(msg);
       //failure message
      }
   });
            $(this).val('');
        }
    }
})

//-- Clear Chat
resetChat();
// {% for i in li %}
//-- Print Messages
// insertChat("me", {{ data[0] }}, 0);
// insertChat("you", "Hi, Pablo", 1500);
// insertChat("me", "What would you like to talk about today?", 3500);
// insertChat("you", "Tell me a joke",7000);
// insertChat("me", "Spaceman: Computer! Computer! Do we bring battery?!", 9500);
// insertChat("you", "LOL", 12000);


//-- NOTE: No use time on insertChat.