<!DOCTYPE HTML>
<html>
	<head>
		<title>Music | Alex's server</title>

		<!-- anchor s tyles -->
		<style>
			a:link,a:visited{
				color:white;
				background-color:#f44336;
				test-decoration:none;
				padding:15px 25px;
				display:inline-block;
			}
			a:hover,a:actve{
				background-color:red;
				cursor:pointer;
			}
		</style>
	</head>

	<body style = "background-color:powderblue;">
		<h1 style = "font-family:verdanan;font-size:300%;text-align:center;">Music Syncing<h1>
		<a href = "index.htm">GO HOME</a>

		<!-- inputes for event time -->
		<input id = "IM">
		<button type = "button" onclick = "setM()">Set Minutes</button>
		<input id = "IS">
		<button type = "button" onclick = "setS()">Set Seconds</button>

		<!-- info place holder -->
		<h2 style = "font-size:150%;" id = "enter">Enter</h2>
		<h3 style = "font-size:150%;" id = "event">Event</h3>
		<h4 style = "font-size:150%;" id = "current">Current</h3>
		<h5 style = "font-size:150%;" id = "isTime"></h3>

		<?php
			//time functions to find server side minutes and seconds
			function getM(){
				$CT = time();
				$M = date("i",$CT);
				return $M;
			}
			function getS(){
				$CT = time();
				$S = date("s",$CT);
				return $S;
			}
			//date time class to find server side Milliseconds
			function getU(){
				$CDT = new DateTime();
				$U = $CDT -> format('v');
				return $U;
			}
		?>

		<script>
			//pass server side time to javascript at the start of the load
			var M = "<?php echo getM()?>";
			var S = "<?php echo getS()?>";
			var U = "<?php echo getU()?>";

			//display default info
			var enter_text = "Enter Minutes: " + M + "   Seconds: " + S + "   Milliseconds: " + U;
			document.getElementById("enter").innerHTML = enter_text;
			var event = [30,0]
			var event_text = "Event Minutes: " + event[0] + "   Seconds: " + event[1];
			document.getElementById("event").innerHTML = event_text;

			//format
			U = Number(U);
			S = Number(S);
			M = Number(M);
			//load audio
			var audio = new Audio("Adrenaline.mp3");
			//uncomment to test audio source
			//audio.play();

			//buttun functions
			function setM(){
				event[0] = document.getElementById("IM").value;
			}
			function setS(){
				event[1] = document.getElementById("IS").value;
			}

			//buffer run WS function every Milliseconds
			buffer = setInterval(WS,1);

			//buffer until the next whole second
			function WS(){
				U = U + 1;
				//temp_current = "buffing: " + U.toString();
			  //document.getElementById("current").innerHTML = temp_current;
				document.getElementById("current").innerHTML = "buffering";
				if(U=>1000){
					//when reach next whole second, stop buffering and start timer function
					clearInterval(buffer);
					setInterval(timer,1000);
					//var audio = new Audio("Adrenaline.mp3");
				}
			}

			//count the second to calculate current time
			function timer(){
				//if the timer reach it's destiny
				if(M == event[0] && S == event[1]){
					document.getElementById("isTime").innerHTML = "Time reached but cannot play music";
					audio.play();
					document.getElementById("isTime").innerHTML = "Playing";
				}

				//seconds and minutes exchange
				S = S + 1;
				if(S == 60){
					S = 0;
					M = M + 1;
				}
				if(M == 60){
					M = 0;
				}

				//display updated current and event info
				event_text = "Event Minutes: " + event[0] + "   Seconds: " + event[1];
				document.getElementById("event").innerHTML = event_text;
				current_text = "Current Minutes: " + M + "   Second: " + S;
				document.getElementById("current").innerHTML = current_text;
			}

		</script>

	</body>

</html>
