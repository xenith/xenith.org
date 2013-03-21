MOUNT_POINT = '/home/vagrant/project'

Vagrant::Config.run do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.forward_port 8000, 8000

    # Increase vagrant's patience during hang-y CentOS bootup
    # see: https://github.com/jedi4ever/veewee/issues/14
    config.ssh.max_tries = 50
    config.ssh.timeout   = 300

    # nfs needs to be explicitly enabled to run.
    config.vm.share_folder("v-root", MOUNT_POINT, ".", :nfs => true)

    # Add to /etc/hosts: 33.33.33.24 dev.example.com
    config.vm.network :hostonly, "33.33.33.24"

    #config.vm.provision :puppet do |puppet|
    #    puppet.manifests_path = "puppet/manifests"
    #    puppet.manifest_file  = "vagrant.pp"
    #end
end
