const axios = require('axios');
const cheerio = require('cheerio');

const fetchHTML = async (url) => {
  try {
    const { data } = await axios.get(url);
    return data;
  } catch (error) {
    console.error(`Error fetching HTML from ${url}: ${error}`);
    return null;
  }
};

const extractMetaTags = (html) => {
  const $ = cheerio.load(html);
  const metaTags = {};

  $('meta').each((i, element) => {
    const name = $(element).attr('name');
    const content = $(element).attr('content');

    if (name && content) {
      metaTags[name] = content;
    }
  });

  return metaTags;
};

const analyzeSEO = async (url) => {
  const html = await fetchHTML(url);
  if (!html) return null;

  const metaTags = extractMetaTags(html);
  return metaTags;
};

module.exports = {
  analyzeSEO,
};