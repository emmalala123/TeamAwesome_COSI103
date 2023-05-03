/*
  jamesPage.js -- Router for the jamesPage
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




isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// generate page before any prompt has been typed
router.get('/jamesPage',
  isLoggedIn,
  async (req, res, next) => {
        const response = ""
        res.render('jamesPage',{response});
});


/* generate the response and render page */
router.post('/jamesPage',
  isLoggedIn,
  async (req, res, next) => {
    const gptResponse = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "Write a poem using the following prompt: " + req.body.prompt,
        max_tokens: 2048,
    });
    const response = gptResponse.data.choices[0].text
    res.render('jamesPage',{response});
});

module.exports = router;