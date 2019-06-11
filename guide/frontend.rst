.. highlight:: javascript

Javascript frontend
===================


Explore the frontend code
-------------------------


Javascript crash course
-----------------------

Functions
~~~~~~~~~

Don't worry :) Javascript is actually pretty simple language – it's the transpilers, libraries, all the browser stuff that sometimes make Javascript look complicated. ::

    function hello(name = 'World') {
      console.info(`Hello, ${name}!`)
    }

    hello("JS")


Above you see a simple "Hello World" program in Javascript. If you run it in Node.js (in your terminal), it prints to the standard output (i.e. to the terminal). If you run it in a web browser (Chrome, Firefox, Edge...) it prints the message to the _developer console_.

☞ Task: Try to put the hello function to the web browfser developer console and run it.

Function is just an object, you can even assign it to a variable directly::

    const hello = function(name) {
      console.info(`Hello, ${name}!`)
    }

    // or using the "arrow-function" syntax:

    const hello = (name) => { 
      console.info(`Hello, ${name}!`) 
    }

    // or just

    const hello = name => console.info(`Hello, ${name}!`)


Objects
~~~~~~~

This is how a Javascript object looks like::

    const apple = {
      color: 'red', 
      about: function() {
        console.info(`This is a ${this.color} apple`)
      },
      describe: () => {
        console.info(`This is a ${this.color} apple`)
      },
    }
    
    console.info(apple.red)
    // prints: red

    // this is another way how to access object properties - kind of like Python getattr
    console.info(apple['red'])
    // prints: red

    apple.about()
    // prints: This is a red apple

    apple.describe()
    // prints: This is a red apple

Have you notices the `this` keyword? It's Javascript magic. When you call `apple.about`, Javascript automatically assigns the `apple` object to `this`. Connection between `this` and `apple` happened just because you have called it this way. See::

    apple.about()
    // prints: This is a red apple

    const aboutApple = apple.about
    aboutApple()
    // prints: This is a undefined apple

    const orange = {
      color: 'orange',
    }
    orange.about = apple.about
    orange.about()
    // prints: This is a orange apple

This is crazy, right? An object "method" should stay connected to the object! And that's exactly what _arrow-functions_ do::

    const describeApple = apple.describe
    describeApple()
    // prints: This is a red apple

    const orange = {
      color: 'orange',
    }
    orange.describe = apple.describe
    orange.describe()
    // prints: This is a red apple


Classes
~~~~~~~

Another thing we are going to need are *classes*. Yes, Javascript has classess! Since 2015 or so :) ::

    class Fruit {

      constructor(type, color) {
        this.type = type
        this.color = color
      }

      about() {
        console.info(`This is a ${this.color} ${this.type}`)
      }

      describe = () => {
        console.info(`This is a ${this.color} ${this.type}`)
      }

    }

    const apple = new Fruit('apple', 'red')

The difference between `about` and `describe` methods are the same as above (in the object example) :)


Introspection
~~~~~~~~~~~~~

If you want to know what some value is or what keys it has, you can just print it::

    console.info(typeof apple)
    // prints: object

    console.info(Object.keys(apple))
    // prints: ["color", "about", "describe"]


Arrays
~~~~~~




React crash course
------------------

Next.js crash course
--------------------


Relay crash course
------------------


Get the frontend working on localhost
-------------------------------------

npm install etc.



Implement the required functionality using React and Relay
----------------------------------------------------------
