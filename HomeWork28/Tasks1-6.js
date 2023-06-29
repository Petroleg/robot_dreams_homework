window.addEventListener('DOMContentLoaded', function() {
  let randomFriendsCount = Math.floor(Math.random() * 1001);
  let addToFriendsButton = document.getElementById('add-friends-button');
  let friendsCountElement = document.getElementById('friends-count');
  let writeMessageButton = document.getElementById('write-message-button');
  let offerJobButton = document.getElementById('offer-job-button');
  let handInHomeworkButton = document.getElementById('hand-in-homework-button');
  let isWriteMessageClicked = false;
  let isOfferJobClicked = false;
  let addToFriendsButtonDisplayStyle = getComputedStyle(addToFriendsButton).display;
  let tableBody = document.querySelector('tbody');

  friendsCountElement.innerHTML = '<h4>Friends: ' + randomFriendsCount + '</h4>';

  function addToFriendsClicked() {
    randomFriendsCount += 1;
    friendsCountElement.innerHTML = '<h4>Friends: ' + randomFriendsCount + '</h4>';
    addToFriendsButton.innerHTML = `
      <div class="spinner-border spinner-border-sm me-2" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      Confirmation Pending
    `;
    addToFriendsButton.disabled = true;
  }

  function writeMessageClicked() {
    if (isWriteMessageClicked) {
      writeMessageButton.classList.remove('btn-warning');
      isWriteMessageClicked = false;
    } else {
      writeMessageButton.classList.add('btn-warning');
      isWriteMessageClicked = true;
    }
  }

  function offerJobClicked() {
    if (isOfferJobClicked) {
      addToFriendsButton.style.display = addToFriendsButtonDisplayStyle;
      isOfferJobClicked = false;
    } else {
      addToFriendsButtonDisplayStyle = getComputedStyle(addToFriendsButton).display;
      addToFriendsButton.style.display = 'none';
      isOfferJobClicked = true;
    }
  }

  function handInHomeworkClicked() {
    let newRow = document.createElement('tr');
    let td1 = document.createElement('td');
    let td2 = document.createElement('td');

    td1.textContent = 'Слава';
    td2.textContent = 'Україні';

    newRow.appendChild(td1);
    newRow.appendChild(td2);
    tableBody.appendChild(newRow);
  }

  addToFriendsButton.addEventListener('click', addToFriendsClicked);
  writeMessageButton.addEventListener('click', writeMessageClicked);
  offerJobButton.addEventListener('click', offerJobClicked);
  handInHomeworkButton.addEventListener('click', handInHomeworkClicked);
});
