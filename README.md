# Python-Scripts

 A central place to store my general purpose python scripts
 
 Typically the scripts are for performing file operations, etc.
 
 <h3>functionsToES6</h3>
 
 A small script for converting files that use ES5 javascript to ES6, for example:
 
 <code>function addTwo(args)</code> is converted to: <code>const addTwo = (args) =></code>.
  
 <h3>inlineReactToCSS</h3>
 
  A script for converting <code>.js</code> files that use inline React styles to <code>.css</code> files:
 
 <p><code>
  const boxStyle = {
    margin: '1rem',
    backgroundColor: 'red'
  }
 </code></p>
 <p>is converted to:</p> 
  <p><code>
  .boxStyle {  
    margin: 1rem;  
    background-color: red;  
  }
 </code></p>
