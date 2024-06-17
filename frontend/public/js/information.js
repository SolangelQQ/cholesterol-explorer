document.addEventListener('DOMContentLoaded', function() {
    const baseUrl = 'http://localhost:5000';

    const graphTypeDropdown = document.getElementById('graph-type');
    const mainGraphContainer = document.getElementById('main-graph');

    fetchAndRenderGraph('age');

    graphTypeDropdown.addEventListener('change', function() {
        const selectedValue = graphTypeDropdown.value;
        fetchAndRenderGraph(selectedValue);
    });

    function fetchAndRenderGraph(graphType) {
        fetch(`${baseUrl}/${graphType}`)
            .then(response => response.json())
            .then(data => {
                if (graphType === 'age') {
                    renderPlotlyHistogram(data);
                } else if (graphType === 'gender') {
                    renderPlotlyBarChart(data);
                } else if (graphType === 'bmi_hba1c') {
                    renderPlotlyScatterPlot(data);
                } else if (graphType === 'cholesterol') {
                    renderPlotlyBoxPlot(data);
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function renderPlotlyHistogram(data) {
        const layout = {
            title: 'Distribución de Edad'
        };
        Plotly.newPlot('main-graph', JSON.parse(data), layout);
    }

    function renderPlotlyBarChart(data) {
        const layout = {
            title: 'Distribución de Género'
        };
        Plotly.newPlot('main-graph', JSON.parse(data), layout);
    }

    function renderPlotlyScatterPlot(data) {
        const layout = {
            title: 'BMI vs HbA1c'
        };
        Plotly.newPlot('main-graph', JSON.parse(data), layout);
    }

    function renderPlotlyBoxPlot(data) {
        const layout = {
            title: 'Niveles de Colesterol Total por Diagnóstico'
        };
        Plotly.newPlot('main-graph', JSON.parse(data), layout);
    }
});
