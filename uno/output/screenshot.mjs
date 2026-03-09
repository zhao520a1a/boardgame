import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();

// ========== 1. 导出 longform 长图 ==========
console.log('📄 正在导出 longform 长图...');
await page.setViewport({ width: 500, height: 800 });
await page.goto('file:///Users/golden/Documents/Qoder/笔记创作/boardgame/uno/output/UNO_长图.html', { waitUntil: 'networkidle0' });
await page.waitForFunction(() => document.fonts.ready);
await new Promise(r => setTimeout(r, 1500));

const card = await page.$('.card');
if (card) {
  await card.screenshot({ path: 'UNO_长图.png', omitBackground: false });
  console.log('✅ 已导出: UNO_长图.png');
}

// ========== 2. 导出 multipage 分页图 ==========
console.log('\n📄 正在导出 multipage 分页图...');
await page.setViewport({ width: 820, height: 1100 });
await page.goto('file:///Users/golden/Documents/Qoder/笔记创作/boardgame/uno/output/UNO_信息图.html', { waitUntil: 'networkidle0' });
await page.waitForFunction(() => document.fonts.ready);
await new Promise(r => setTimeout(r, 1500));

const pages = await page.$$('.page');
for (let i = 0; i < pages.length; i++) {
  const filename = `UNO_P${i + 1}.png`;
  await pages[i].screenshot({ path: filename, omitBackground: false });
  console.log(`✅ 已导出: ${filename}`);
}

await browser.close();
console.log('\n🎉 全部导出完成！');
