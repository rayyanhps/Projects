function sendAsPDF() {
	const ss = SpreadsheetApp.getActiveSpreadsheet();
	const sheet = ss.getActiveSheet();
	const sh = ss.getSheets()[0];
  // Detect send trigger, that will later match with e-mail IF condition
	const svalue = sh.getRange(2, 17).getValue();
  // Email Details
	const sender = Session.getEffectiveUser().getEmail();
	const recipientClient = SpreadsheetApp.getActiveSheet().getRange(1, 6).getValue() + "," + sender;
	const recipientBCC = "name@propertypro.co.id" + "," + "name@propertypro.co.id"; // BCC should be e-mail of manager and e-mail of BD 
	const subject = "PropertyPRO: " + SpreadsheetApp.getActiveSheet().getRange(8, 3).getValue();
	const subjectF = "Failure to Send " + SpreadsheetApp.getActiveSheet().getRange(8, 3).getValue();
	const pdfName =  SpreadsheetApp.getActiveSheet().getRange(8, 3).getValue();
  // body email 
	const body = html
  	const html =
	    '<body>' + 
	      'Dear ' + SpreadsheetApp.getActiveSheet().getRange(1, 17).getValue() + ',' +
		'<br><br>' +
		  '<p>Bersama ini kami lampirkan analisa dan rekomendasi kami untuk pembelian anda di: <br>' +
		  '<table="width:50%;"><tr>' +
		  '<td>Lokasi</td><td>:</td>' +
		  '<td>' + SpreadsheetApp.getActiveSheet().getRange(20, 9).getDisplayValue() + '</td>' +  
		'</tr>' +
		'<tr>' +
		  '<td>Harga</td><td>:</td>' +
		  '<td>' + SpreadsheetApp.getActiveSheet().getRange(21, 9).getDisplayValue() + '</td>' +  
		'</tr></table><br>' +
		  'Apabila ada pertanyaan silahkan menghubungi kami melalui kontak yang tercantum di bagian bawah laporan terlampir.' + 
		  'Terima kasih.' + 
		'<br><br></p>' +
		  '<p>Salam,<br><b><font style="color:navy;">' + SpreadsheetApp.getActiveSheet().getRange(2, 6).getValue() + 
		    '<br></b>Financial Advisor<br></font></p>' +
	   '</body>'
        
	const bodyF = htmlF
	const htmlF =
	    '<body>' + 
	      'Hey team,' +
		'<br><br>' +
		'<p> We have exceeded the daily mail quota. Please check it. Or... you have inputted something incorrect.</p>' +
		'<p>Thanks</p>' +
	   '</body>'
              
	const ssId = ss.getId()  
	const sheetId = sh ? ss.getSheets()[0].getSheetId() : null;  
	const url_base = ss.getUrl().replace(/edit$/,'');
	const url_ext = 'export?exportFormat=pdf&format=pdf'   //export as pdf
	+ (sheetId ? ('&gid=' + sheetId) : ('&id=' + spreadsheetId)) 
	+ '&size=A4'      // paper size
	+ '&portrait=true'    // orientation, false for landscape
	+ '&fitw=true'        // fit to width, false for actual size
	+ '&sheetnames=false&printtitle=false&pagenumbers=false'  //hide optional headers and footers
	+ '&gridlines=false'  // hide gridlines
	+ '&fzr=false'       // do not repeat row headers (frozen rows) on each page
	+ '&ir=false'        // the lines below have things to do with the range import
	+ '&ic=false'
	+ '&c1=0'       // defines the starting column 
	+ '&r1=3'       // defines the starting row
	+ '&c2=28'        // defines the ending column
	+ '&r2=77';       // defines the ending row
	const options = {
		headers: {
        		'Authorization': 'Bearer ' +  ScriptApp.getOAuthToken(),
		}
	}

	const response = UrlFetchApp.fetch(url_base + url_ext, options);
	const cldoc = response.getBlob().setName(pdfName + '.pdf'); 

	//Check if the send trigger is correctly inputted 
        if (svalue == "X"  && sheet.getName() == "CL" && MailApp.getRemainingDailyQuota() > 0)
	//Send the Email
		MailApp.sendEmail(recipientClient, subject, body, {
			htmlBody: html, attachments: cldoc
		}
	 )
        else ( //message sent back if something is wrong
		MailApp.sendEmail(sender, subjectF, body, {
        		htmlBody: htmlF
		}
	)
);

//End of sendAsPDF//
}
