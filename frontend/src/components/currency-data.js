const CurrencyData = (props) => {
  const {effective_date, mid} = props.data
  
  return (
    <div>
      <div className="currency-data"> 
      Kurs <span>{mid}</span>
      na dzień <span>{effective_date}</span>
      </div>
    </div>
  )
}

export default CurrencyData;
