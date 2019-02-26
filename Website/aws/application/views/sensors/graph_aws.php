<div class="row no-gutters">
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = google.visualization.arrayToDataTable([
                [ { label: 'date', type: 'date' },
                { label_:'<?php echo $title?>' } ],

                <?php
                foreach ($values as $row) {
                    $date = $row['date']['S'] . " " . $row['time']['S'];
                    $date1 = date_create($date);
                    $date2 = "Date(".date_format($date1, 'Y').", ".((int) date_format($date1, 'm') - 1).", ".date_format($date1, 'd').", ".date_format($date1, 'H').", ".date_format($date1, 'i').", ".date_format($date1, 's').")";
                    echo "['" . $date2 . "', ".$row[$sensor]['N']."],";
                }
                ?>
            ]);

            var options = {
                title: '<?php echo $title?>',
                //curveType: 'function',
                vAxis: {
                    //minValue: <?php echo $min?> ,
                    //maxValue: <?php echo $max?> ,
                    title: "<?php echo $unit?>",
                    minorGridlines: {
                        count: 0,
                    },
                },
                hAxis: {
                    title: 'Time',
                    format: "HH:mm",
                    minorGridlines: {
                        count: 0,
                    },
                },
                legend: { position: 'none' },
                chartArea : { left: "20%" , right: "10%", top: "10%", bottom: "12%"}
            };

            // Customize tooltip format
            var date_formatter = new google.visualization.DateFormat({
                pattern: "HH:mm"
            });
            date_formatter.format(data, 0);  // Where 0 is the index of the column

            var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
            chart.draw(data, options);
        }

        $(window).resize(function(){
            drawChart();
        });
        </script>
    </head>

    <body>
        <div id="curve_chart" style="width: 100vw; height: calc(100vh - 56px)"></div>
    </body>
</div>
