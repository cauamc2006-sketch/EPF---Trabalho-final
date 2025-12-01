% rebase('layout.tpl')

<div class="container mt-5">
    % if defined('categoria'):
        <h2 class="text-center mb-4">Categoria: {{categoria}}</h2>
    % else:
        <h2 class="text-center mb-4">Todos os Jogos</h2>
    % end


    % if jogos:
        <div class="row g-4 justify-content-center">

            % for j in jogos:
                <div class="col-12 col-md-4 col-lg-3">
                    <div class="card shadow-sm bg-dark text-light text-center p-2">
                        
                        <img src="{{j.get_imagem()}}" class="card-img-top" alt="imagem" style="object-fit:cover; height:180px;">

                        <div class="card-body">
                            <h5 class="card-title">{{j.get_nome()}}</h5>
                            <p class="card-text">{{j.get_genero()}}</p>

                            <a href="/jogo/{{j.get_id()}}" class="btn btn-success w-100">
                                Ver detalhes
                            </a>
                        </div>
                    </div>
                </div>
            % end

        </div>
    % else:
        <div class="alert alert-warning text-center">
            Nenhum jogo nessa categoria.
        </div>
    % end
</div>

