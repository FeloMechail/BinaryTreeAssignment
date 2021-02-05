$.ajaxSetup({ cache:false });
var previous = null;
    var current = null;
    setInterval(function() {
        $.getJSON('static/read.json', function(data) {
            console.log(`TEMPERATURE: ${data.temperature}`)
            console.log(`HUMIDITY: ${data.humidity}`)
            console.log(`MINT: ${data.mint}`)
            console.log(`BASIL: ${data.basil}`)
            console.log(`MINTS: ${data.mints}`)
            console.log(`PARSELY: ${data.ros}`)
            console.log(`ROSEMARY: ${data.pars}`)
            $('#ID50').text(data.temperature)
            $('#ID10').text(data.humidity)
            $('#ID20').text(data.mint)
            $('#ID30').text(data.mints)
            $('#ID40').text(data.pars)
            $('#ID70').text(data.basil)
            $('#ID60').text(data.ros)
            
        });                       
    }, 2000); 