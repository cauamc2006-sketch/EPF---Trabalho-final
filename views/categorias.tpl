% rebase('layout.tpl')

<div class="container mt-4">
    <h2 class="mb-4 text-center">Categorias</h2>

    % if categorias:
        <div class="row g-3">
            % for cat in categorias:
                <div class="col-12 col-md-4">
                    <a href="/categorias/{{cat}}" style="text-decoration:none;">
                        <div class="card shadow-sm p-3 text-center">
                            <h5 class="text-primary">{{cat}}</h5>
                        </div>
                    </a>
                </div>
            % end
        </div>
    % else:
        <div class="alert alert-warning text-center">
            Nenhuma categoria encontrada.
        </div>
    % end
</div>

