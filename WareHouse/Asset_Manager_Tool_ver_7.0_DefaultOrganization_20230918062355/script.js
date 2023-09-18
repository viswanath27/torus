'''
Create a Flask application showing the Apple stock data with its patterns explained with the help of Candlestick chart, bar chart, line chart and figure chart. Use Yfinance library in python to read the stock data for APPLE organization.
'''
document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('chart').getContext('2d');
    var symbol = document.getElementById('symbol').value;
    fetch('/stock_data', {
        method: 'POST',
        body: new URLSearchParams({
            'symbol': symbol
        })
    })
    .then(response => response.json())
    .then(data => {
        var dates = Object.keys(data);
        var prices = Object.values(data).map(obj => obj['Close']);
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Closing Price',
                    data: prices,
                    borderColor: 'blue',
                    fill: false
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Price'
                        }
                    }
                }
            }
        });
    })
    .catch(error => console.log(error));
});