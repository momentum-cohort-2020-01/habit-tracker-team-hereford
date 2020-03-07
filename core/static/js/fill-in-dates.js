/* requires moment */

const dateCells = document.querySelectorAll('.date')
const initLength = dateCells.length
const dataHolder = document.querySelector('#data-holder')
const habitPK = dataHolder.dataset.pk
const owner = dataHolder.dataset.owner
const user = dataHolder.dataset.user


if (initLength > 1) {
  const firstDate = moment(dateCells[0].textContent, 'MMMM D, YYYY')
  const lastDate = moment(dateCells[initLength - 1].textContent, 'MMMM D, YYYY')

  for (let day = firstDate; day.isAfter(lastDate); day.subtract(1, 'days')) {
    const prevDay = day.clone()
    prevDay.add(1, 'days')
    const dateString = day.format('MMMM D, YYYY')
    const cell = document.querySelector(`[data-date='${dateString}']`)
    if (cell == null) {
      addRow(prevDay, day)
    }
  }
}
else {
  const titleRow = document.querySelector('tr')
  const rowBelow = document.createElement('tr')
  if (owner === user) {
    rowBelow.innerHTML = `<td></td><td class="achievement"><a href="/add-record?habit=${habitPK}">Add a record</a></td>`
    titleRow.insertAdjacentElement('afterend', rowBelow)
  }
}

function addRow (prevDay, day) {
  const prevDayString = prevDay.format('MMMM D, YYYY')
  const dayString = day.format('MMMM D, YYYY')
  const urlDayString = day.format('YYYY-MM-DD')
  const rowAbove = document.querySelector(`[data-date='${prevDayString}']`).closest('tr')
  const rowBelow = document.createElement('tr')
  if (owner === user) {
    rowBelow.innerHTML = `<td class="date" data-date="${dayString}">${dayString}</td>
    <td class="achievement"><a href="/add-record?habit=${habitPK}&date=${urlDayString}">Add a record</a></td>`
  }
  else {
    rowBelow.innerHTML = `<td class="date" data-date="${dayString}">${dayString}</td>
    <td class="achievement">No record</td>`
  }
  rowAbove.insertAdjacentElement('afterend', rowBelow)
}