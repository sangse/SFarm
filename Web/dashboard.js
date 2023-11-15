/* globals Chart:false */






///(() => {

  
  'use strict'
  

  
  //Firebase 데이터베이스 만들기
  const firebaseConfig = {
    apiKey: "AIzaSyD1e4-uze8Lk0FtDMcKVTagK_2zw2vapec",
    authDomain: "fir-25fa9.firebaseapp.com",
    databaseURL: "https://fir-25fa9-default-rtdb.firebaseio.com",
    projectId: "fir-25fa9",
    storageBucket: "fir-25fa9.appspot.com",
    messagingSenderId: "782015119942",
    appId: "1:782015119942:web:3f8aca666c609c44d48047",
    measurementId: "G-0QQSC92WK5"
  };

  
  firebase.initializeApp(firebaseConfig);
  const database = firebase.database();
  const firebaseRef = firebase.database().ref('data');
  function ledON() {
    var ref = database.ref('led');
    ref.update({ led: 1 })
  }

  function ledOFF() {
    var ref = database.ref('led');
    ref.update({ led: 0 })
  }

  
  firebaseRef.orderByKey().limitToLast(20).once('value')
    .then(snapshot => {
      const dataFromFirebase = snapshot.val();

      const labels = Object.keys(dataFromFirebase);
      const humidityData = Object.values(dataFromFirebase).map(entry => entry.humidity);
      const luxData = Object.values(dataFromFirebase).map(entry => entry.lux);
      const temperatureData = Object.values(dataFromFirebase).map(entry => entry.temperature);

      myChart.data.labels = labels;
      myChart1.data.labels = labels;
      myChart2.data.labels = labels;
      myChart.data.datasets[0].data = temperatureData;
      myChart1.data.datasets[0].data = humidityData;
      myChart2.data.datasets[0].data = luxData;

      myChart.update();
      myChart1.update();
      myChart2.update();
    })
    .catch(error => {
      console.error('Error fetching data from Firebase:', error);
    });

  // Graphs
  const ctx = document.getElementById('myChart')
  const ctx1 = document.getElementById('myChart1')
  const ctx2 = document.getElementById('myChart2')
  // eslint-disable-next-line no-unused-vars

  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'
        ],
        datasets: [{
            data: [1, 2, 3, 4],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#ffeb3b', // Change the border color to yellow
            borderWidth: 4,
            pointBackgroundColor: '#ffeb3b', // Change the point color to yellow
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                boxPadding: 3
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time' // Add the Temperature label for the x-axis
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Temperature' // You can customize the y-axis label if needed
                }
            }
        }
    }
});

  const myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
     labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [1,2,3,4],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'

      }
       ]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          boxPadding: 3
        }
      },
      scales: {
          x: {
              title: {
                  display: true,
                  text: 'Time' // Add the Temperature label for the x-axis
              }
          },
          y: {
              title: {
                  display: true,
                  text: 'Humidity' // You can customize the y-axis label if needed
              }
          }
      }
      
      
    }
    
  })
  const myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
     labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [1,2,3,4],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'

      }
       ]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          boxPadding: 3
        }
      },
      scales: {
          x: {
              title: {
                  display: true,
                  text: 'Time' 
              }
          },
          y: {
              title: {
                  display: true,
                  text: 'Lux'
          }
      }
    }
  }
  })
///})()
