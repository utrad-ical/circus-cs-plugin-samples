/**
 * CIRCUS CS Plugin Sample - Hello World
 */

const path = rquire('path');
const fs = require('fs').promises;

const outDir = '/circus/out';
const outFile = path.join(outDir, 'results.json');
const inDir = '/circus/in';

const result = {
  metadata: {
    displayOptions: [
      {
        volumeId: 0,
        window: { level: -600, width: 1500 },
        crop: { origin: [76, 139, 26], size: [331, 215, 215] }
      }
    ]
  },
  results: {
    lesionCandidates: [
      {
        rank: 1,
        confidence: 0.8380112051963806,
        volumeId: 0,
        location: [200, 258, 58],
        volumeSize: 885.4866027832031
      }
    ]
  }
};

const main = async () => {
  await fs.writeFile(outFile, JSON.stringify(result), 'utf8');
};

main();
