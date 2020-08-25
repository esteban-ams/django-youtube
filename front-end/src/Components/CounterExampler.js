import React, { useState } from "react";

function CounterExplample() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>{count}</h1>
      <h1 onClick={() => setCount(count + 5)}>
        <strong> + with your hand </strong>
      </h1>
      <h1 onClick={() => setCount(count - 4)}>
        <strong> - with a Fork </strong>
      </h1>
    </div>
  );
}

export default CounterExplample;
