# XMPFilter

Integration of `xmpfilter` to sublime text 2 as a plugin.

## Installation

You have 3 options for installing XMPFilter Plugin: using Package Control, using Git, or just downloading it.

### Package Control

Inside Sublime Text 2, open your command pallete (⌘ + ⇧ + P on OS X), and select "Package Control: Install Package".

After this, search for "XMPFilter" and install it!

### Git

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X

    ```shell
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ```

* Linux

    ```shell
    cd ~/.Sublime\ Text 2/Packages/
    ```

* Windows

    ```shell
    cd %APPDATA%/Sublime Text 2/Packages/
    ```

After this, you just need to clone this repository:

```shell
git clone git://github.com/kassi/sublime-text-2-xmpfilter.git XMPFilter
```

### Download

Click on the nice cloud icon above and download the zip file containing this plugin.

Then unzip the file and move the resulting folder to your Packages directory.

## Usage

Open a ruby file and add a ruby marker right behind or below any statement.

```ruby
x = 123 * 45 # =>
y = x - 6789
# =>
```

Now run the command `Execute And Update Ruby Markers` from your command pallete (⌘ + ⇧ + P on OS X).

Or simply hit the pre-defined keyboard shortcut (⌥ + ⌘ + B on OS X).

Watch your code getting annotated.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Author

Karsten Silkenbäumer

[![endorse](http://api.coderwall.com/ksi/endorsecount.png)](http://coderwall.com/ksi)
