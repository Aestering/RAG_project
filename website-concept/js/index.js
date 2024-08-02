import * as deepl from 'deepl-node';

const authKey = process.env['DEEPL_AUTH_KEY'];
const serverUrl = process.env['DEEPL_SERVER_URL'];
const translator = new deepl.Translator(authKey, { serverUrl: serverUrl });

(async () => {
    try {
        console.log(await translator.getUsage());

        const result = await translator.translateText('Hello, world!', null, 'fr');

        console.log(result.text); // Bonjour, le monde !
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
})();


