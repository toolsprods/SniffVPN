var datastatics = "", datalogs = "";
var totalanalyzed = 0, malicious = 0;

function onLoad() {
	datastatics = getFile("data/vtanalyzer.json");
	datalogs = getFile("data/logs.json");

	$(".sidenavitem").css("width", $("#item0").width());
	$(".navbaritem").css("width", $("#navbarhead").width());
	
	$("#dbanalysgraph").hide();
	$("#dbanalysgraph").fadeIn(3000);
	goDashboard();
}

function resize() {
	$(".sidenavitem").css("width", $("#item0").width());
	$(".navbaritem").css("width", $("#navbarhead").width());

	getGraphics(totalanalyzed, malicious);
}

function goDashboard() {
	$("#overviewpanel").show();
	$("#staticspanel").hide();
	$("#logspanel").hide();
	
	$("*").removeClass("itemactive");
	$("#item0").addClass("itemactive");
	
	$("*").removeClass("navitemactive");
	$("#navitem0").addClass("navitemactive");

	totalanalyzed = 0;
	malicious = 0;

	datastatics = getFile("data/vtanalyzer.json");
	if (datastatics) {
		var statics = '{"vtanalyzer":[' + datastatics.slice(0, datastatics.length-1) + ']}';
		statics = JSON.parse(statics);
		var lengthstatics = statics.vtanalyzer.length;
		var liststatics = '<table class="cl">';

		for(i = lengthstatics-1; i >= 0; i--) {
			if (statics.vtanalyzer[i].positives != undefined){
				totalanalyzed += 1;
				if (statics.vtanalyzer[i].positives != 0) {
					malicious += 1;
					liststatics += '<tr><td>' + statics.vtanalyzer[i].url + '</td></tr>'
				}
			}
		}
		liststatics += '</table>';

		document.getElementById("dbanalyslist").innerHTML = liststatics;
		document.getElementById("dbanalys").innerHTML = totalanalyzed + " URLs analyzed, " + malicious + " URLs malicious";
		getGraphics(totalanalyzed, malicious);
	}
	else
		document.getElementById("dbanalyslist").innerHTML = "<h4>No info available</h4>";

	datalogs = getFile("data/logs.json");
	if (datalogs) {
		var logs = '{"logs":[' + datalogs.slice(0, datalogs.length-1) + ']}';
		logs = JSON.parse(logs);
		var lengthlogs = logs.logs.length;
		var listlogs = '<table class="cl">';

		for(i = lengthlogs-1; i > (lengthlogs-6); i--) {
			listlogs += '<tr><td>' + logs.logs[i].url + '</td></tr>';
		}
		listlogs += '</table>';

		document.getElementById("dbvisitlist").innerHTML = listlogs;
		document.getElementById("dbvisit").innerHTML = "Total: " + lengthlogs+" URLs visited";
	} else 
		document.getElementById("dbvisitlist").innerHTML = "<h4>No info available</h4>";
}

function goStatistics() {
	$("#staticspanel").show();
	$("#overviewpanel").hide();
	$("#logspanel").hide();
	
	$("*").removeClass("itemactive");
	$("#item1").addClass("itemactive");
	
	$("*").removeClass("navitemactive");
	$("#navitem1").addClass("navitemactive");

	tableStatics(0);

	datastatics = getFile("data/vtanalyzer.json");

	if (datastatics) {
		var data = '{"vtanalyzer":[' + datastatics.slice(0, datastatics.length-1) + ']}';
		data = JSON.parse(data);

		var itemsperpage = 10;
		var length = 0;
		for (i = 0; i < data.vtanalyzer.length; i++) {
			if (data.vtanalyzer[i].positives != undefined){
				if (data.vtanalyzer[i].positives == 0)
					length += 1;
			}
		}
		getPaginationSize(itemsperpage, length);
		}
	else
		document.getElementById("tablestatics").innerHTML = "<h3>There aren´t statics yet</h3>";
}

function goLogs() {
	$("#logspanel").show();
	$("#overviewpanel").hide();
	$("#staticspanel").hide();

	$("*").removeClass("itemactive");
	$("#item2").addClass("itemactive");

	$("*").removeClass("navitemactive");
	$("#navitem2").addClass("navitemactive");

	tableLogs(0);

	datalogs = getFile("data/logs.json");

	if (datalogs) {
		var data = '{"logs":[' + datalogs.slice(0, datalogs.length-1) + ']}';
		data = JSON.parse(data);

		var itemsperpage = 10;
		getPaginationSize(itemsperpage, data.logs.length);
	}
	else
		document.getElementById("tablelogs").innerHTML = "<h3>There aren´t logs</h3>";
}

function getFile(file) {
	var xhttp = new XMLHttpRequest();
	xhttp.open("GET", file, false);
	try {
		xhttp.send();
		return xhttp.responseText;
	}
	catch(err) {
		return false;
	}
}

function getGraphics(total, malicious) {
	$("#dbanalysgraph").attr("width", $("#dbanalys").width());
	var max = $("#dbanalysgraph").width();
	var mal = (malicious * 100) / total;
	mal = max * (mal / 100);

	var canvas = document.getElementById("dbanalysgraph");
	var ctx = canvas.getContext("2d");
	ctx.lineWidth="10";
	ctx.beginPath();
	ctx.strokeStyle="#2EB83A"; //Green path
	ctx.moveTo(0, 10);
	ctx.lineTo(max, 10);
	ctx.stroke(); //Draw it

	ctx.beginPath();
	ctx.strokeStyle="#BF2600"; //Red path
	ctx.moveTo(0,10);
	ctx.lineTo(mal,10);
	ctx.stroke(); //Draw it
}

function tableStatics(page) {
	datastatics = getFile("data/vtanalyzer.json");

	if (datastatics) {
		var data = '{"vtanalyzer":[' + datastatics.slice(0, datastatics.length-1) + ']}';
		data = JSON.parse(data);

		var itemsperpage = 10;
		var from = page * itemsperpage;
		var to = from + itemsperpage;

		var table = '<table class="cl"><tr><th>URL</th><th style="width: 10%">VT Scan</th></tr>';
		for(i = from; i < to; i++) {
			if (data.vtanalyzer[i].positives != undefined){
				if (data.vtanalyzer[i].positives == 0)
					var result = '<h4 style="color: #2EB83A" class="glyphicon glyphicon-ok"></h4>'
				else
					var result = '<h4 style="color: #BF2600" class="material-icons">error_outline</h4>'
				table += '<tr><td><a href="https://www.virustotal.com' + data.vtanalyzer[i].reanalyse_url +
				'" target="_blank">' + data.vtanalyzer[i].url + '</a></td>' +
				'<td>' + result + '</td></tr>'
			}
			else
				if (to < data.vtanalyzer.length)
					to += 1
		}
		table += '</table>';

		document.getElementById("tablestatics").innerHTML = table;
		}
	else
		document.getElementById("tablestatics").innerHTML = "<h3>There aren´t statics yet</h3>";
}

function tableLogs(page) {
	datalogs = getFile("data/logs.json");

	if (datalogs) {
		var data = '{"logs":[' + datalogs.slice(0, datalogs.length-1) + ']}';
		data = JSON.parse(data);

		var itemsperpage = 10;
		var from = page * itemsperpage;
		var to = from + itemsperpage;

		var table = '<table class="cl"><tr><th style="width: 15%">Time</th><th style="width: 12%">Original IP</th><th style="width: 12%">IP Source</th><th style="width: 12%">IP Destiny</th><th>URL</th></tr>';
		for(i = from; i < to; i++) {
			table += '<tr><td>' + data.logs[i].time +
			'</td><td>' + data.logs[i].iporig +
			'</td><td>' + data.logs[i].ipsrc +
			'</td><td>' + data.logs[i].ipdst +
			'</td><td><a href="http://' + data.logs[i].url + '" target="_blank">' + data.logs[i].url + '</a></td></tr>'
		}
		table += '</table>';

		document.getElementById("tablelogs").innerHTML = table;
	}
	else
		document.getElementById("tablelogs").innerHTML = "<h3>There aren´t logs</h3>";
}

function getPaginationSize(items, length) {
	var size = length / items;

	$('#paginationlogs, #paginationstatics').bootpag({
        total: size,
		page: 1,
		maxVisible: 10,
		leaps: true,
		firstLastUse: true,
		first: '←',
		last: '→',
		wrapClass: 'pagination',
		activeClass: 'active',
		disabledClass: 'disabled',
		nextClass: 'next',
		prevClass: 'prev',
		lastClass: 'last',
		firstClass: 'first'
        }).on("page", function(event, num){
			tableLogs(num-1);
			tableStatics(num-1);
        });
}