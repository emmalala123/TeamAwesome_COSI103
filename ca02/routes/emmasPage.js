/*
  willsPage.js -- Router for the willsPage
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User')

const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config()

const configuration = new Configuration({
    apiKey: process.env.APIKEY,
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
router.get('/emmasPage',
  isLoggedIn,
  async (req, res, next) => {
        const response = ""
        res.render('emmasPage',{response});
});


/* generate the response and render page */
router.post('/emmasPage',
  isLoggedIn,
  async (req, res, next) => {
    const gptResponse = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "Please generate a CSS file for the following color scheme: " + req.body.prompt,
        max_tokens: 2048,
    });
    const response = gptResponse.data.choices[0].text
    res.render('emmasPage',{response});
});

module.exports = router;