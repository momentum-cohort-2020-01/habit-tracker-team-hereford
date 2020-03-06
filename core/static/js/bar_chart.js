// var chart = {
//   type: 'horizontalbar',
//   data: {
//     datasets: [{
//       data: {{ data|safe }},
//       backgroundColor:'#E4FF1A',
//       barPercentage: 0.5,
//       barThickness: 6,
//       maxBarThickness: 8,
//       minBarLength: 2,
//       data: [10, 20, 30, 40, 50, 60, 70]
//     }],
//       label: 'Habit'
//     },
//     labels: {{ labels|safe }}
//   },
//   options = {
//     scales: {
//         xAxes: [{
//             gridLines: {
//                 offsetGridLines: true
//             }
//         }]
//     }
// };


var config = {
  type: 'horizontalbar',
  data: {
    labels: {{ labels|safe }},
    datasets: [{
      label: 'Habit',
      backgroundColor: 'blue',
      data: {{ data|safe }}
    }]          
  },
  options: {
    scales: {
      yAxes: [{
        gridLines: {
          offsetGridLines: true
            }
        }]
    }
  }
    responsive: true,
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Your Habit History'
    }
  }

  window.onload = function() {
  var ctx = document.getElementById('bar_chart').getContext('2d');
  window.myPie = new Chart(ctx, config);
};