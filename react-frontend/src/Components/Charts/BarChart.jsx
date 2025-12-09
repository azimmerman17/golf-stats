import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, Ticks } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend );

const BarChart = ({ chartData, borderWidth, dataLabel, axis, min, max, step }) => {
  let labels = []
  let values = []

  chartData.forEach(item => {
    const { label, value } = item
    labels.push(label)
    values.push(value)
  })

  const options = {
    indexAxis: axis,
    elements: {
      bar: {
        borderWidth: borderWidth,
      },
    },

    responsive: true,
    plugins: {
      // legend: {
      //   position: 'right',
      // },
    },
  };

  // add the custom scale on correct axis
  if (axis === 'y') {
    options.scales = {
      x: {
        beginAtZero: false,
        max,
        min
      }
    }
  } else {
    options.scales = {
      y: {
        beginAtZero: false,
        max,
        min
      }
    }
  }

const data = {
  labels,
  datasets: [{
      label: dataLabel,
      data: values,
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
   }],
};

return <Bar options={options} data={data} />;
  
}

export default BarChart