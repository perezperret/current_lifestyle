document.getElementById('payment-form').addEventListener('submit', (e) => {
  e.preventDefault()
  const form = e.target

  fetch(form.action, { method: form.method, body: new FormData(form) })
    .then(response => response.json())
    .then(result => {
      const preview = document.getElementById('result-preview')
      const format = new Intl.NumberFormat('en-US', {
        style: 'currency', currency: 'USD'
      }).format
      preview.style.display = 'block'
      preview.innerHTML = [
        `<p>You would need a monthly payout of <strong>${format(result.real_retirement_pmt)}</strong> during retirement.</p>`,
        `<p>You would need a fund with <strong>${format(result.retirement_fund)}</strong> by the time you retire.</p>`,
        `<p>You should save <strong>${format(result.saving_payment)}</strong> for retirement every month.</p>`
      ].join("\n\n")
    })
})
