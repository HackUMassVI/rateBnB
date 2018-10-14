	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    	var tab = tabs[0];
	
	var bool= tab.url.includes("airbnb.com/rooms");
	document.querySelector(".frame1").style.display="none";

	if(bool)
	{

	document.querySelector(".frame2").style.display="none";
	document.querySelector(".frame1").style.display="block";

	const xhttp = new XMLHttpRequest();
	var modURL= tab.url.substr(8);
	
	var temp = "";
	for (var i = 0; i < modURL.length ; i++) {
		if(modURL.charAt(i)=='?'){
			break;
		}
		temp += modURL.charAt(i);
	}
	var modURL1="https://"+temp;
	var finalURL= "http://67.205.146.104:5000/scoreListChrome?url="+modURL1;
	var link = document.getElementById("redir");
    link.setAttribute('href', finalURL);
	
	console.log(temp);
	xhttp.open("GET", "http://67.205.146.104/chrome_get?url="+temp, true);
	xhttp.onreadystatechange = function()
	{
	    if(xhttp.readyState == 4 && xhttp.status == 200) {
	    
	    	document.querySelector(".frame2").style.display="block";
			document.querySelector(".frame1").style.display="none";
	    	var response = xhttp.responseText;

			var rating= parseInt(response)/20;//Some formula or API sends it
			const starTotal=5;
			const starPercentage = (rating/starTotal)*100;
			const starPercentageRounded = (Math.round(starPercentage/10)*10);
			document.querySelector(".stars-inner").style.width = starPercentageRounded*3/4;
			console.log(starPercentageRounded);
		}

	    }
	xhttp.send(null);
	}
});