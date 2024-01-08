//feedback
let feedbackBtn = document.getElementById("feedback-btn");
let feedbackDiv = document.getElementById("feedback-div");
let listItems = ["Click 2 cards to turn them over and reveal their monsters.",
    "If the monsters match, they stay turned over.", "If they do not match the cards are turned back.",
    "Keep going until all the monsters are turned over.",
    "Try to remember where you have seen which monsters, so you can use them to make a match."
];

// Grid
let gridContainerDiv = document.getElementById("grid-container-div");
let gridContainer = document.createElement("div");
let monsters = [
    { src: "./assets/images/demon.png", alt: "Demon", dataName: "Demon" },
    { src: "./assets/images/frankenstein.png", alt: "Frankenstein", dataName: "Frankenstein" },
    { src: "./assets/images/clown.png", alt: "Clown", dataName: "Clown" },
    { src: "./assets/images/mummy.png", alt: "Mummy", dataName: "Mummy" },
    { src: "./assets/images/vampire.png", alt: "Vampire", dataName: "Vampire" },
    { src: "./assets/images/death.png", alt: "Death", dataName: "Death" },
    { src: "./assets/images/ghost.png", alt: "Ghost", dataName: "Ghost" },
    { src: "./assets/images/zombie.png", alt: "Zombie", dataName: "Zombie" },
    { src: "./assets/images/demon.png", alt: "Demon", dataName: "Demon" },
    { src: "./assets/images/frankenstein.png", alt: "Frankenstein", dataName: "Frankenstein" },
    { src: "./assets/images/clown.png", alt: "Clown", dataName: "Clown" },
    { src: "./assets/images/mummy.png", alt: "Mummy", dataName: "Mummy" },
    { src: "./assets/images/vampire.png", alt: "Vampire", dataName: "Vampire" },
    { src: "./assets/images/death.png", alt: "Death", dataName: "Death" },
    { src: "./assets/images/ghost.png", alt: "Ghost", dataName: "Ghost" },
    { src: "./assets/images/zombie.png", alt: "Zombie", dataName: "Zombie" },
];

//Timer
let timerId;
let timer;
let timerSpan = document.getElementById('timer');
let timerStarted = false;

//Moves
var moves = 0;

// Flip Cards
let cards = document.getElementsByClassName("card");
let hasFlippedCard = false;
let lockBoard = false;
let firstCard, secondCard;
// True to enable, false to disable clicks,
let freezeClicks = false;

//Restart
let restartBtn = document.getElementById("restart-btn");

//Event Listeners
feedbackBtn.addEventListener("click", feedbackBtnClick);
restartBtn.addEventListener("click", reset);

//feedback 

/** Function opens the feedback div
 * Once the feedback button is clicked and the div has appeared it is disabled to stop it opening more feedback div underneath the the current one.
 * feedback appear in a numbered list
 * A close button is added that, when clicked, removes the feedback div.
 */
function feedbackBtnClick(event) {

    //Disable feedback button after being clicked
    document.getElementById("feedback-btn").disabled = true;

    // Create the a Div
    let feedback = document.createElement("div");

    // Put the Div inside the HTML element feedback-div
    feedbackDiv.appendChild(feedback);

    // Put a h3 element inside the new Div
    let feedbackHeading = document.createElement("h3");
    feedbackHeading.innerHTML = "feedback:";
    feedback.appendChild(feedbackHeading);

    // Create and put an ordered list under the h3 element
    let feedbackList = document.createElement("ol");

    for (let i = 0; i < listItems.length; i++) {
        let listItem = document.createElement("li");
        listItem.innerHTML = listItems[i];
        feedbackList.appendChild(listItem);
    }

    feedback.appendChild(feedbackList);

    //Create the button
    let closeBtn = document.createElement("button");
    closeBtn.classList.add("close-btn");
    feedback.appendChild(closeBtn);
    closeBtn.innerHTML = "Close";

    /**
     * Function is run when button is clicked. 
     * It removes the feedback div.
     */
    function closeBtnClick(event) {
        feedbackDiv.removeChild(feedback);
        document.getElementById("feedback-btn").disabled = false;
    }
    closeBtn.addEventListener("click", closeBtnClick);
}

// Grid
gridContainer.classList.add("grid-container");
gridContainerDiv.appendChild(gridContainer);

/** Shuffle monsters
 * Monsters are shuffled using the Fisher Yates method
 */
const shuffleMonsters = monsters => {
    for (let i = monsters.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let k = monsters[i];
        monsters[i] = monsters[j];
        monsters[j] = k;
    }
};
shuffleMonsters(monsters);

for (let monster of monsters) {
    let card = document.createElement("div");
    card.classList.add("card");

    let monsterImg = document.createElement("img");
    monsterImg.src = monster.src;
    monsterImg.alt = monster.alt;
    monsterImg.dataset.dataName = monster.dataName;
    monsterImg.classList.add("card-front");

    card.appendChild(monsterImg);

    gridContainer.appendChild(card);

    let backImg = document.createElement("img");
    backImg.src = "./assets/images/pumpkin.png";
    backImg.alt = "pmupkin";
    backImg.classList.add("card-back");

    card.appendChild(backImg);
}

//Timer

/** 
 * Function starts timer when first card is clicked and increments by 1 every second
 */
function startTimer() {
    if (timerStarted) return;
    timer = 0;
    timerId = setInterval(() => {
        timerSpan.innerHTML = " " + timer + "s";
        timer++;
    }, 1000);
    timerStarted = true;
}

// Flip Cards

/**
 * Function for flipping cards
 * When the first card is flipped the timer starts.
 * Each card flip is counted as a move which increments by one.
 * When the second card is flipped, if there is no match, the board is locked for 1 sec, the same time it takes to unflip the cards.
 * checkForMatch function is run.
 */
function flipCard() {
    // Check if the card is already flipped
    if (this.isFlipped) return;

    // Check if the click events are frozen
    if (freezeClicks) return;

    // Set the card state to flipped
    this.isFlipped = true;

    moves++;

    document.querySelector("#moves").textContent = " " + moves;

    if (lockBoard) return;
    if (this === firstCard) return;

    this.classList.toggle("flip");

    if (!hasFlippedCard) {
        //First click
        hasFlippedCard = true;
        firstCard = this;
        startTimer();
        return;
    }

    //Second click

    secondCard = this;

    freezeClicks = true;

    checkForMatch();
}

/**
 * Function to see if the two selected cards match
 * Checks the dataName for both cards and checks to see if whether or not they are the same.
 * If they are the same a div element will pop up giving the user their score of time and moves.
 * If the cards match disableCards() is called and freezeClicks set to false in order to allow clicks again.
 * If the cards don't match the cards are flipped back.
*/
function checkForMatch() {

    let firstDataName = firstCard.children[0].dataset.dataName;
    let secondDataName = secondCard.children[0].dataset.dataName;

    let isMatch = firstDataName === secondDataName;

    const popUp = document.getElementById("pop-up");
    const youWinDiv = document.createElement("div");
    const youWin = document.createElement("h3");
    const result = document.createElement("p");
    const closeBtn = document.createElement("button");

    if (isMatch) {
        disableCards(); freezeClicks = false;
    } else { unflipCards(); }

    //You Win popup when game is over
    if (document.querySelectorAll('.flip').length === cards.length) {
        clearInterval(timerId); // stop the timer

        popUp.appendChild(youWinDiv);
        youWinDiv.classList.add("you-win-div");

        youWin.innerHTML = "You Win!";
        youWinDiv.appendChild(youWin);

        result.innerHTML = (`It only took ${timer} seconds <br> and ${moves} moves! `);
        youWinDiv.appendChild(result);

        closeBtn.classList.add("close-btn");
        youWinDiv.appendChild(closeBtn);
        closeBtn.innerHTML = "Close";
    }
    /** 
     * Function is run when button is clicked. 
     * It removes the You Win div.
    */
    function closeBtnClick(event) {
        popUp.removeChild(youWinDiv);
    }
    closeBtn.addEventListener("click", closeBtnClick);
}

/**
 * Function is run when the pair of cards match.
 * It stops the cards from being clicked again.
 * The board is then reset and the next pair is ready to be chosen.
 */
function disableCards() {
    firstCard.removeEventListener("click", flipCard);
    secondCard.removeEventListener("click", flipCard);

    firstCard.isFlipped = false;
    secondCard.isFlipped = false;

    resetBoard();
}

/**
 * Function is run when the pair of cards don't match.
 * The board is set to be locked for one second.
 * The selected cards flip back in one second.
 * The board is then reset and the next pair is ready to be chosen.
 */
function unflipCards() {
    lockBoard = true;

    setTimeout(() => freezeClicks = false, 1000);

    setTimeout(() => {
        firstCard.classList.remove('flip');
        secondCard.classList.remove('flip');

        firstCard.isFlipped = false;
        secondCard.isFlipped = false;

        resetBoard();
    }, 1000);
}

/**
 * Resets board back to how it was before the last two clicks
 * flips the cards back over and sets their values to null
 */
function resetBoard() {
    [hasFlippedCard, lockBoard] = [false, false];
    [firstCard, secondCard] = [null, null];
}

for (let card of cards) {
    card.addEventListener("click", flipCard);
}

//Restart Button

/** Refreshes the web browser when the user selects "Restart"
 */
function reset() {
    location.reload();
}

