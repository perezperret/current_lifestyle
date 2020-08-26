document.getElementById('payment-form').addEventListener('submit', (e) => {
  e.preventDefault()

  values = []
  formData = new FormData(e.target)
  for (var key of formData.keys()) {
    values.push([key, formData.get(key)])
  }

  query = values.map(([value, name]) => {
    if (value && name) { return `${value}=${name}` }
  }).filter(i => i).join('&');

  fetch(`${e.target.action}?${query}`)
    .then(response => response.json())
    .then(result => {
      const preview = document.getElementById('result-preview')
      const format = new Intl.NumberFormat('en-US', {
        style: 'currency', currency: 'USD'
      }).format
      preview.style.display = 'block'
      preview.innerText = [
        `You would need a monthly payout equivalent to USD ${format(result.real_retirement_pmt)} during retirement.`,
        `You would need a fund with USD ${format(result.retirement_fund)}.`,
        `You should pay in USD ${format(result.saving_payment)} every month.`
      ].join("\n\n")
    })
})