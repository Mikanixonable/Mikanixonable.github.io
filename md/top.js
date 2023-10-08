const audioElements = {};
function btn(filePath, button) {
  if (!audioElements[filePath]) {
      // 新しい音声ファイルを再生
      audioElements[filePath] = new Audio(filePath);
      audioElements[filePath].play();
      button.classList.add('playing'); // ボタンのスタイルを変更
      // 音声再生終了時のイベントハンドラを設定
      audioElements[filePath].addEventListener('ended', function() {
          button.classList.remove('playing'); // ボタンのスタイルを元に戻す
          delete audioElements[filePath]; // オブジェクトから削除
      });} else {
      // 既存の音声ファイルを停止
      audioElements[filePath].pause();
      audioElements[filePath].currentTime = 0; // 音声を最初から再生できるようにリセット
      delete audioElements[filePath]; // オブジェクトから削除
      button.classList.remove('playing'); // ボタンのスタイルを元に戻す
  }}