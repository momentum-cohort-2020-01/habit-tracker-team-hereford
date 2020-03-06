/* requires moment */

let dateCells = document.querySelectorAll('.date')

if (dateCells.length > 1) {
  let dateObjects = []

  for (const cell of dateCells) {
    const dateString = cell.textContent
    const dateObject = moment(dateString, 'MMMM DD, YYYY')
    dateObjects.push(dateObject)
  }

  for (const date of dateObjects) {
    let nextDate = date.clone()
    nextDate.subtract(1, 'days')
    if (!dateObjects.includes(nextDate)) {
      const idx = dateObjects.indexOf(date)
      dateObjects.splice(idx + 1, 0, nextDate)
    }
  }

  for (const date in dateObjects) {

  }
}

function addRow (dateObj) {
  const dateString = dateObj.format('MMMM DD, YYYY')
  console.log(dateString)
  const rowAbove = document.querySelector(`[data-date='${dateString}']`)
  const rowBelow = document.createElement('tr')
  rowBelow.innerHTML = `<td class="date" data-date="${dateString}">${dateString}</td>
  <td class="achievement"><a href="{% url 'add_habit_record' habit.pk %}">Add a record</a></td>`
  rowAbove.insertAdjacentElement('afterend', rowBelow)
}

// dateCell = document.createElement('td')
// achvCell = document.createElement('td')
// dateCell.classList.add('date')
// dateCell.setAttribute('data-date', dateString)
// dateCell.textContent = dateString
// achvCell.classList.add('achievement')
// formLink = document.createElement('a')
// formLink