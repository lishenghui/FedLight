pushd ../docs
  rm -rf ./build
  make html
  rm -rf ~/Desktop/bladesteam.github.io/*
  cp -rf ./build/html/* ~/Desktop/bladesteam.github.io/
popd
pushd ~/Desktop/bladesteam.github.io/
  git add .
  git commit -m "update"
  git push
popd