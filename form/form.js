const numOptionsSelect = document.getElementById('numOptions');
const optionsContainer = document.getElementById('optionsContainer');

numOptionsSelect.addEventListener('change', generateOptions);

function generateOptions() {
    const numOptions = parseInt(numOptionsSelect.value);
    optionsContainer.innerHTML = '';

    for (let i = 1; i <= numOptions; i++) {
        const optionDiv = document.createElement('div');

        const optionLabel = document.createElement('label');
        optionLabel.textContent = `Option ${i}:`;
        optionDiv.appendChild(optionLabel);

        const optionNameInput = document.createElement('input');
        optionNameInput.type = 'text';
        optionNameInput.name = `optionName${i}`;
        optionNameInput.placeholder = 'Medicine Name';
        optionDiv.appendChild(optionNameInput);

        const optionAmountSelect = document.createElement('select');
        optionAmountSelect.name = `optionAmount${i}`;
        const amounts = [1, 2, 3]; // Modify these as needed
        amounts.forEach((amount) => {
            const option = document.createElement('option');
            option.value = amount;
            option.textContent = `${amount}`;
            optionAmountSelect.appendChild(option);
        });
        optionDiv.appendChild(optionAmountSelect);

        const optionDaysSelect = document.createElement('select');
        optionDaysSelect.name = `optionDays${i}`;
        for (let days = 1; days <= 7; days++) {
            const option = document.createElement('option');
            option.value = days;
            option.textContent = `${days} days`;
            optionDaysSelect.appendChild(option);
        }
        optionDiv.appendChild(optionDaysSelect);

        const attributeCount = parseInt(optionAmountSelect.value);
        for (let j = 1; j <= attributeCount; j++) {
            const attributeInput = document.createElement('input');
            attributeInput.type = 'text';
            attributeInput.name = `optionAttribute${i}_${j}`;
            attributeInput.placeholder = `Time ${j}`;
            optionDiv.appendChild(attributeInput);
        }

        optionAmountSelect.addEventListener('change', () => {
            const newAttributeCount = parseInt(optionAmountSelect.value);
            const attributeInputs = optionDiv.querySelectorAll('input[name^="optionAttribute"]');
            attributeInputs.forEach((input) => {
                input.remove();
            });

            for (let j = 1; j <= newAttributeCount; j++) {
                const attributeInput = document.createElement('input');
                attributeInput.type = 'text';
                attributeInput.name = `optionAttribute${i}_${j}`;
                attributeInput.placeholder = `Attribute ${j}`;
                optionDiv.appendChild(attributeInput);
            }
        });

        optionsContainer.appendChild(optionDiv);
    }
}

// Initial generation
generateOptions();
