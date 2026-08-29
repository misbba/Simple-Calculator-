/**
 * script.js - Smart Calculator Client-side Interactions
 *
 * Handles operation button clicks, dynamic num2 input toggling,
 * AJAX calculation requests, keyboard support, and clear history confirmation.
 */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Element References
    const calcForm = document.getElementById('calculator-form');
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const num2Group = document.getElementById('num2-group');
    const selectedOpInput = document.getElementById('selected-op-input');
    const opBtns = document.querySelectorAll('.op-btn');
    
    const errorBox = document.getElementById('error-box');
    const errorMessage = document.getElementById('error-message');
    
    const resultBox = document.getElementById('result-box');
    const resultValue = document.getElementById('result-value');
    const equationValue = document.getElementById('equation-value');
    
    const historyContainer = document.getElementById('history-container');
    const clearHistoryForm = document.getElementById('clear-history-form');

    /**
     * Updates UI state depending on selected operation
     * Disables second number input if operation is 'square_root'
     */
    function updateOperationUI(op) {
        selectedOpInput.value = op;

        // Update active class on operation buttons
        opBtns.forEach(btn => {
            if (btn.dataset.op === op) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Toggle num2 visibility/disabled state for single-operand operations (square_root)
        if (op === 'square_root') {
            num2Input.disabled = true;
            num2Input.required = false;
            num2Input.value = '';
            num2Group.classList.add('disabled');
        } else {
            num2Input.disabled = false;
            num2Input.required = true;
            num2Group.classList.remove('disabled');
        }
    }

    // Attach click listeners to Operation Buttons
    opBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const op = btn.dataset.op;
            updateOperationUI(op);
        });
    });

    // Initialize state on load
    updateOperationUI(selectedOpInput.value || 'add');

    /**
     * Display error alert message
     */
    function showError(msg) {
        errorMessage.textContent = msg;
        errorBox.classList.remove('hidden');
    }

    /**
     * Hide error alert message
     */
    function hideError() {
        errorMessage.textContent = '';
        errorBox.classList.add('hidden');
    }

    /**
     * Render updated calculation history list dynamically
     */
    function updateHistoryUI(historyList) {
        if (!historyList || historyList.length === 0) {
            historyContainer.innerHTML = '<p class="empty-history" id="empty-history-msg">No calculations performed yet.</p>';
            if (clearHistoryForm) {
                clearHistoryForm.style.display = 'none';
            }
            return;
        }

        let html = '<ol class="history-list">';
        historyList.forEach(item => {
            html += `<li class="history-item">${escapeHtml(item)}</li>`;
        });
        html += '</ol>';
        historyContainer.innerHTML = html;

        if (clearHistoryForm) {
            clearHistoryForm.style.display = 'block';
        }
    }

    /**
     * Helper to escape HTML characters for safety
     */
    function escapeHtml(str) {
        return str.replace(/[&<>"']/g, (m) => {
            return {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            }[m];
        });
    }

    /**
     * Handles Form Submission via AJAX (Fetch API)
     */
    calcForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideError();

        const num1Val = num1Input.value.trim();
        const num2Val = num2Input.value.trim();
        const operationVal = selectedOpInput.value;

        // Basic Client-side Validation
        if (!num1Val) {
            showError('Please enter a valid number.');
            return;
        }

        if (operationVal !== 'square_root' && !num2Val) {
            showError('Please enter a valid second number.');
            return;
        }

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    num1: num1Val,
                    num2: num2Val,
                    operation: operationVal
                })
            });

            const data = await response.json();

            if (data.success) {
                // Show Result Box
                resultValue.textContent = data.result;
                if (equationValue) {
                    equationValue.textContent = data.equation;
                }
                resultBox.classList.remove('hidden');

                // Update History Log
                updateHistoryUI(data.history);
            } else {
                showError(data.error || 'Calculation failed.');
            }
        } catch (err) {
            console.error('Fetch error:', err);
            // Fallback: submit form normally if network error occurs
            calcForm.submit();
        }
    });

    /**
     * Confirm Before Clearing History
     */
    if (clearHistoryForm) {
        clearHistoryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const confirmed = confirm('Are you sure you want to clear your calculation history?');
            if (confirmed) {
                try {
                    const response = await fetch('/clear-history', {
                        method: 'POST',
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });
                    const data = await response.json();
                    if (data.success) {
                        updateHistoryUI([]);
                        resultBox.classList.add('hidden');
                        hideError();
                    }
                } catch (err) {
                    clearHistoryForm.submit();
                }
            }
        });
    }
});
