/*
  todo.js -- Router for the ToDoList
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User')

const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config()

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
const openai = new OpenAIApi(configuration);


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/willsPage',
  isLoggedIn,
  async (req, res, next) => {
        const response = ""
        res.render('willsPage',{response});
});


/* add the value in the body to the list associated to the key */
router.post('/willsPage',
  isLoggedIn,
  async (req, res, next) => {
    const gptResponse = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: req.body.prompt,
    });
    const response = gptResponse.data.choices[0].text
    res.render('willsPage',{response});
});

module.exports = router;