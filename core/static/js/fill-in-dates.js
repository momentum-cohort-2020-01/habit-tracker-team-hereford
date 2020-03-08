/* requires moment */

const dateCells = document.querySelectorAll('.date')
const initLength = dateCells.length
const dataHolder = document.querySelector('#data-holder')
const habitPK = dataHolder.dataset.pk
const owner = dataHolder.dataset.owner
const user = dataHolder.dataset.user
const dateFormat = 'YYYY-MM-DD'

if (initLength > 1) {
  const firstDate = moment(dateCells[0].dataset.date, dateFormat) // Grab date from data-attr, not the cell
  const lastDate = moment(dateCells[initLength - 1].dataset.date, dateFormat)

  for (let day = firstDate; day.isAfter(lastDate); day.subtract(1, 'days')) {
    const prevDay = day.clone()
    prevDay.add(1, 'days')
    const dateString = day.format(dateFormat)
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
  const prevDayString = prevDay.format(dateFormat)
  const dayString = day.format('MMMM D, YYYY')
  // const dataDayString = day.format('YYYY-MM-DD')
  const urlDayString = day.format(dateFormat)
  const rowAbove = document.querySelector(`[data-date='${prevDayString}']`).closest('tr')
  const rowBelow = document.createElement('tr')
  if (owner === user) {
    rowBelow.innerHTML = `<td class="date" data-date="${urlDayString}">${dayString}</td>
    <td class="achievement"><a href="/add-record?habit=${habitPK}&date=${urlDayString}">Add a record</a></td>`
  }
  else {
    rowBelow.innerHTML = `<td class="date" data-date="${urlDayString}">${dayString}</td>
    <td class="achievement">No record</td>`
  }
  rowAbove.insertAdjacentElement('afterend', rowBelow)
}
