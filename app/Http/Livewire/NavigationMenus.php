<?php

namespace App\Http\Livewire;

use App\Models\NavigationMenu;
use Livewire\Component;
use Livewire\WithPagination;

class NavigationMenus extends Component
{
    use WithPagination;

    public $modalFormVisible;
    public $modalConfirmDeleteVisible;

    public $modelId;
    public $label;
    public $slug;
    public $sequence = 1;
    public $type = 'SidebarNav';



    /**
     * The validation rules
     *
     * @return void
     * */
    public function rules()
    {
        return [
            'label' => 'required',
            'slug' => 'required',
            'sequence' => 'required',
            'type' => 'required',
        ];
    }


    /**
     * The read function for navigation menu
     *
     * @return void
     * */
    public function read()
    {
        return NavigationMenu::paginate(5);
    }


    /**
     * The update function for the navigation menus
     *
     * @return void
     * */
    public function update()
    {
        $this->validate();
        NavigationMenu::find($this->modelId)->update($this->modelData());
        $this->modalFormVisible = false;
    }

    /**
     * The delete function for the navigation menus
     *
     * @return void
     * */
    public function delete()
    {
        NavigationMenu::destroy($this->modelId);
        $this->modalConfirmDeleteVisible = false;
        $this->resetPage();
    }


    /**
     * The create function for nav menu items
     *
     * @return void
     * */
    public function create()
    {
        $this->validate();
        NavigationMenu::create($this->modelData());
        $this->modalFormVisible = false;
        $this->reset();
    }


    /**
     * Creates and spawns a modal in the frontend for menu items
     * management
     *
     * @return void
     * */
    public function createShowModal()
    {
        $this->resetValidation();
        $this->reset();
        $this->modalFormVisible = true;
    }

    /**
     * Shows the form modal in update mode
     *
     * @param mixed $id
     * @return void
     * */
    public function updateShowModal($id)
    {
        $this->resetValidation();
        $this->reset();
        $this->modalFormVisible = true;
        $this->modelId = $id;
        $this->loadModel();
    }

    /**
     * Deletes the model data of the current component
     *
     * @param mixed $id
     * @return void
     * */
    public function deleteShowModal($id)
    {
        $this->modelId = $id;
        $this->modalConfirmDeleteVisible = true;
    }

    /**
     * Loads the model data
     * of this component
     *
     * @return void
     * */
    public function loadModel()
    {
        $data = NavigationMenu::find($this->modelId);
        $this->label = $data->label;
        $this->slug = $data->slug;
        $this->type = $data->type;
        $this->sequence = $data->sequence;
    }


    /**
     * The data for the model mapped in this component.
     *
     * @return void
     * */
    public function modelData()
    {
        return [
            'label' => $this->label,
            'slug' => $this->slug,
            'sequence' => $this->sequence,
            'type' => $this->type
        ];
    }

    public function render()
    {
        return view('livewire.navigation-menus', [
            'data'=> $this->read(),
        ]);
    }
}
