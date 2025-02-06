document.addEventListener('DOMContentLoaded', function() {
    fetch('resultado_estadistica.csv')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la càrrega del fitxer CSV');
            }
            return response.text();
        })
        .then(data => {
            console.log('Dades del CSV:', data); // Mostra les dades del CSV a la consola
            const rows = data.split('\n'); // Separa les files
            const taula = document.getElementById('taula-dades');

            // Crear la taula
            const table = document.createElement('table');
            table.style.width = '100%';
            table.setAttribute('border', '1');
            table.setAttribute('cellpadding', '5');
            table.setAttribute('cellspacing', '0');

            // Crear la capçalera de la taula
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');
            const headers = rows[0].split(','); // La primera fila conté les capçaleres

            headers.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header.trim(); // Neteja els espais en blanc
                headerRow.appendChild(th);
            });

            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Crear el cos de la taula
            const tbody = document.createElement('tbody');

            for (let i = 1; i < rows.length; i++) { // Comença des de la segona fila
                const columns = rows[i].split(',');
                if (columns.length >= 6) { // Verifica que la fila tingui suficents columnes
                    const tr = document.createElement('tr');

                    columns.forEach(column => {
                        const td = document.createElement('td');
                        td.textContent = column.trim(); // Neteja els espais en blanc
                        tr.appendChild(td);
                    });

                    tbody.appendChild(tr);
                }
            }

            table.appendChild(tbody);
            taula.appendChild(table); // Afegir la taula al div

            // Crear les gràfiques
            const years = [];
            const totals = [];
            const medias = [];
            const maximas = [];
            const minimas = [];
            const variaciones = [];

            for (let i = 1; i < rows.length; i++) {
                const columns = rows[i].split(',');
                if (columns.length >= 6) {
                    years.push(columns[0]);
                    totals.push(parseFloat(columns[1]));
                    medias.push(parseFloat(columns[2]));
                    maximas.push(parseFloat(columns[3]));
                    minimas.push(parseFloat(columns[4]));
                    const variacion = columns[5] ? parseFloat(columns[5]) : null;
                    variaciones.push(variacion);
                }
            }

            createChart('graficaTotal', 'Total per any', years, totals);
            createChart('graficaMedia', 'Mitjana per any', years, medias);
            createChart('graficaMaxima', 'Màxima mensual per any', years, maximas);
            createChart('graficaMinima', 'Mínima mensual per any', years, minimas);
            createChart('graficaVariacion', 'Variació per any', years, variaciones);
        })
        .catch(error => {
            console.error('Error llegint el fitxer CSV:', error);
            document.getElementById('taula-dades').textContent = 'Error carregant les dades.';
        });
});

function createChart(canvasId, label, labels, data) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}