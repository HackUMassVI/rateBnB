//content.js
	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    	var tab = tabs[0];
	
	
	const xhttp = new XMLHttpRequest();
	var modURL= tab.url.substr(8);
	var temp = "";
	for (var i = 0; i < modURL.length ; i++) {
		if(modURL.charAt(i)=='?'){
			break;
		}
		temp += modURL.charAt(i);
	}
	console.log(temp);
	xhttp.open("GET", "http://67.205.146.104/chrome_get?url="+temp, true);
	xhttp.onreadystatechange = function()
	{
	    if(xhttp.readyState == 4 && xhttp.status == 200) {
	    var response = xhttp.responseText;
	    var bool= tab.url.includes("airbnb.com/rooms");

	    if(bool)
		{		
			var rating= parseInt(response)/20;//Some formula or API sends it
			const starTotal=5;
			const starPercentage = (rating/starTotal)*100;
			const starPercentageRounded = (Math.round(starPercentage/10)*10);
			document.querySelector(".stars-inner").style.width = starPercentageRounded*3/4;
			console.log(starPercentageRounded);
		}

	    }
	}
	xhttp.send(null);
	
	

});