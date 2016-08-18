MeCab python module

$Id: README,v 1.1.1.1 2005/12/03 14:18:50 taku-ku Exp $;

1. Installation
  Only you have to do is python setup.py install (Because source is already built). 
  But you have to modify mecab.h as below
  http://seesaawiki.jp/spz/d/Windows%A4%CBmecab-python%A4%F2%C6%B3%C6%FE

```
/**
 * Lattice class
 */
class MECAB_DLL_CLASS_EXTERN Lattice {
public:

  virtual void set_result(const char *str)        = 0; //この１行を追加

  /**
   * Clear all internal lattice data.
   */
  virtual void clear()              = 0;
```

(you can get modified file from `header` folder in this repository)

  % python setup.py build
  % su
  # python setup.py install
  
  You can change the install directory with the --prefix option. For example:

  % python setup.py install --prefix=/tmp/pybuild/foobar
  
 
2. How to use?

   see 'test.py' as a sample program.
