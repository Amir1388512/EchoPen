// Initial sample data for the chart
var initialData = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",  'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [{
        label: 'Sample Data',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        data: [3,40,50,10,80]
    }]
};

// Configuration options
var options = {
    animation: {
        duration: 5000 
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }
};

// Get the context of the canvas element we want to select
var ctx = document.getElementById("barChart").getContext("2d");

// Create the bar chart with initial data and options
var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: initialData,
    options: options
});

var data = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",  'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [{
        label: 'Sample Data',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        data: [3,40,50,10,80]
    }]
};

// Configuration options
var options = {
    animation: {
            tension: {
              duration: 1000,
              easing: 'linear',
              from: 1,
              to: 0,
              loop: true
            }
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }
};

// Get the context of the canvas element we want to select
var ctx = document.getElementById("lineChart").getContext("2d");

// Create the line chart
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
});