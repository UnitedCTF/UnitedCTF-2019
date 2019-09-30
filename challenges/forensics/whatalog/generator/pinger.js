const axios = require('axios');

const NUMBER_OF_WORDS = 10;

const flagIndex = Math.round(Math.random() * NUMBER_OF_WORDS);

const flag = 'flag-$0N7b3Nvv31rd¢3510G1@k01';

const {
  length
} = flag;

const randomString = () => {
  let result = '';
  for (let i = 0; i < length; i++) {
    const char = String.fromCharCode(Math.round(Math.random() * 93) + 33);
    result += char;
  }

  return result;
}

const toBinaryString = (string) => {
  console.log(string)
  let result = "";
  for (let i = 0; i < string.length; i++) {
    let byte = string.charCodeAt(i).toString(2);
    while (byte.length < 8) {
      byte = `0${byte}`;
    }
    result += byte
  }

  return result;
}

const call = async () => {
  for (let i = 0; i < NUMBER_OF_WORDS; i++) {
    let text = toBinaryString(i === flagIndex ? flag : randomString());

    for (let j = 0; j < text.length; j++) {
      await axios.get(`http://localhost:3000/?q=${text[j]}`);
    }
  }
}

call().then(() => {
  console.log('done')
})