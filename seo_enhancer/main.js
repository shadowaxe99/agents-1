const axios = require('axios');
const cheerio = require('cheerio');

const utils = require('./utils');

const analyzeSEO = async (url) => {
    try {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);

        const seoData = {
            title: $('head > title').text(),
            metaDescription: $('head > meta[name="description"]').attr('content'),
            h1Count: $('h1').length,
            h2Count: $('h2').length,
            imgWithoutAltCount: $('img:not([alt])').length,
            canonicalLink: $('head > link[rel="canonical"]').attr('href'),
        };

        utils.checkSEO(seoData);
    } catch (error) {
        console.error(`Failed to analyze SEO for ${url}: ${error}`);
    }
};

module.exports = { analyzeSEO };