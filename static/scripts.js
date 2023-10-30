document.addEventListener('DOMContentLoaded', function () {
    // Select the mood tracking form and relevant elements
    const moodForm = document.querySelector('#mood-form');
    const moodNotesInput = document.getElementById('mood-notes');
    const moodDisplay = document.querySelector('#mood-display');

    // Select the journal entry form and relevant elements
    const journalForm = document.querySelector('#journal-form');
    const journalContentInput = document.getElementById('journal-content');
    const journalDisplay = document.querySelector('#journal-display');

    // Add an event listener to the mood tracking form submission
    moodForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Get the selected mood type and mood notes
        const selectedMood = document.querySelector('input[name="mood"]:checked');
        
        if (selectedMood) {
            const moodValue = selectedMood.value;

            // Update the UI to display the selected mood and mood notes
            moodDisplay.textContent = `Today's mood: ${moodValue}`;
            moodNotesInput.value = ''; // Clear the mood notes input field
        }
    });

    // Add an event listener to the journal entry form submission
    journalForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Get the journal content
        const journalEntry = journalContentInput.value;

        // Display the journal entry
        journalDisplay.innerHTML += `<p>${journalEntry}</p>`;

        // Clear the journal content input field
        journalContentInput.value = '';
    });
});

